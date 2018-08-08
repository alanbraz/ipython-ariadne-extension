class Ariadne(object):

    def __init__(self, ip):
        self.shell = ip
        self.ok_cells = [ ]
        ip.run_cell("import os\nif 'PYTHONPATH' in os.environ:\n    os.environ['MYPYPATH'] = os.environ['PYTHONPATH']")
        self.initial_cell_index = len(self.shell.user_ns["In"])

    def check(self):
        import urllib.request
        import sys, json, base64, traceback
        # print("Adriane DEBUG: user_ns", self.shell.user_ns)
        current_cell = self.shell.user_ns["In"][-1]
        # print("current_cell", current_cell)
        current_cell_lines = []
        removed_lines = 0
        for line in current_cell.split("\n"):
            # ignore magic commands
            if "get_ipython" not in line:
                current_cell_lines.append(line)
            else:
                removed_lines += 1
        if len(current_cell_lines) > 0:
            current_cell = "\n".join(current_cell_lines)
            cells_to_run_array = self.ok_cells + [current_cell]

            # print("Adriane DEBUG: cells_to_run!")
            # print("cells_to_run", cells_to_run)
            # cells_to_run_array = cells_to_run.split("\n")
            # for i in range(len(cells_to_run_array)):
            #     print('{}: {}'.format(i+1, cells_to_run_array[i].strip()))

            linesJSON = []
            total_lines = 0
            for cell_index in range(len(cells_to_run_array)):
                lines = cells_to_run_array[cell_index].split("\n")
                for line_index in range(len(lines)):
                    total_lines += 1
                    linesJSON.append({ "cell": (cell_index+self.initial_cell_index), "cell_line": line_index+1, "total_line":total_lines, "text": lines[line_index] })
            # print("Adriane DEBUG: linesJSON \n", json.dumps(linesJSON, indent=2))

            # prepare to call the IBM Cloud Function
            cells_to_run = "\n".join(cells_to_run_array)
            body = {"code": cells_to_run }
            myurl = "https://openwhisk.ng.bluemix.net/api/v1/namespaces/Project%20Runway_sandbox/actions/typesForML?blocking=true"
            apiKey = "aa8e9b0b-707b-4548-8dbf-3c53ebc84d78:0wthlpdXBkxO91YVzFIzt27cvUSXaXexiYK7HaKJA9LP5QxWMSPTbyKd4qYSl3Lz"
            req = urllib.request.Request(myurl)
            req.add_header('Content-Type', 'application/json; charset=utf-8')
            base64string = base64.standard_b64encode(apiKey.encode('utf-8'))
            req.add_header("Authorization", "Basic %s" % base64string.decode('utf-8'))
            jsondata = json.dumps(body)
            #print(jsondata)
            jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
            req.add_header('Content-Length', len(jsondataasbytes))
            #print (jsondataasbytes)

            # call IBM Function
            reply = None
            try:
                reply = urllib.request.urlopen(req, jsondataasbytes).read()
            except:
                e = sys.exc_info()[0]
                print("Adriane ERROR calling IBM Function: %s" % e, file=sys.stderr)
                print(traceback.format_exc(), file=sys.stderr)
                print("jsondata: " + json.dumps(jsondata, indent=2), file=sys.stderr)
                return

            diagnostic = None
            data = None
            try:
                data = reply.decode('utf-8')
                data = json.loads(data)
                result = data["response"]["result"]["diagnostic"]
                # print(json.dumps(data["response"]["result"]["diagnostic"], indent=2), file=sys.stderr)
                diagnostic = json.loads(result).get("fakecode.py", None)
                # print(json.dumps(diagnostic, indent=2), file=sys.stderr)
            except:
                e = sys.exc_info()[0]
                print("Adriane ERROR parsing IBM Function results: %s" % e, file=sys.stderr)
                print(traceback.format_exc(), file=sys.stderr)
                print(json.dumps(data, indent=2), file=sys.stderr)
                return

            if diagnostic is not None:
                # print(json.dumps(diagnostic, indent=2), file=sys.stderr)
                for diag in diagnostic:
                    if diag["severity"] != "Information":
                        error_message = None
                        # start
                        error_column_number = diag["range"]["start"]["character"]
                        error_line_number = diag["range"]["start"]["line"]
                        # end
                        error_end_column_number = diag["range"]["end"]["character"]
                        error_end_line_number = diag["range"]["end"]["line"]
                        # print("Adriane DEBUG: error_line_number: " + str(error_line_number))

                        error_line = linesJSON[error_line_number]
                        # print("Adriane DEBUG: error_line", json.dumps(error_line, indent=2))

                        # error_cell_line_number = error_line_number - len(("\n".join(self.ok_cells)).split("\n"))
                        # print("Adriane DEBUG: error_cell_line_number: " + str(error_cell_line_number))

                        line_label = "Cell ["+ str(error_line["cell"]) +"] "+"Line "+ str(error_line["cell_line"]+removed_lines) + ": "
                        error_message = "Adriane Diagnostic "+diag["severity"]+": " + diag["message"] + "\n"
                        line_text = error_line["text"]
                        line_text_trim = line_text.strip()
                        error_message += line_label + line_text_trim
                        white_spaces = len(line_text)-len(line_text_trim)
                        # print("Adriane DEBUG: cells_to_run: " + cells_to_run, file=sys.stderr
                        error_message += "\n" + (len(line_label)+white_spaces+error_column_number)*" " + (error_end_column_number-error_column_number+1)*"^"
                        # print("Adriane DEBUG::\n"+json.dumps(diag, indent=2), file=sys.stderr)
                        if error_message is not None:
                            print(error_message, file=sys.stderr)
                        else:
                            print("Adriane DEBUG: check OK!")
                            self.ok_cells.append(current_cell)
            else:
                print("Adriane DEBUG: check OK!")
                self.ok_cells.append(current_cell)
