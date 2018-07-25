class Ariadne(object):

    def __init__(self, ip):
        self.shell = ip
        self.ok_cells = [ "import os", "os.environ['MYPYPATH'] = os.environ['PYTHONPATH']" ]
        ip.run_cell("\n".join(self.ok_cells))

    def check(self):
        import urllib.request
        import sys, json, base64, traceback
        cells = self.shell.user_ns["In"]
        # print("cells", cells)
        current_cell = cells[-1]
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
            cells_to_run = "\n".join(self.ok_cells + [current_cell])

            # prepare to call the IBM Cloud Function
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
                error_message = None
                for diag in diagnostic:
                    if diag["severity"] == "Error":
                        error_column_number = diag["range"]["start"]["character"]
                        # print("Adriane DEBUG error_column_number: " + str(error_column_number), file=sys.stderr)
                        error_line_number = diag["range"]["start"]["line"]
                        # print("Adriane DEBUG error_line_number: " + str(error_line_number), file=sys.stderr)
                        error_cell_line_number = error_line_number - len(("\n".join(self.ok_cells)).split("\n"))
                        print("Adriane DEBUG error_cell_line_number: " + str(error_cell_line_number), file=sys.stderr)
                        line_label = "Line "+ str(error_cell_line_number+removed_lines) + ": "
                        error_message = "Adriane diagnostic error: " + diag["message"] + "\n"
                        print("Adriane DEBUG current_cell: " + current_cell, file=sys.stderr)
                        current_cell_array = current_cell.split("\n")
                        print("Adriane DEBUG current_cell_array: " + current_cell_array, file=sys.stderr)
                        error_message += line_label + current_cell_array[error_cell_line_number-1]

                        # print("Adriane DEBUG cells_to_run: " + cells_to_run, file=sys.stderr
                        error_message += "\n" + len(line_label)*" "+ (error_column_number-1)*" " + "^"
                        # print("Adriane DEBUG:\n"+json.dumps(diag, indent=2), file=sys.stderr)
                if error_message is not None:
                    print(error_message, file=sys.stderr)
                else:
                    print("Adriane DEBUG check OK with Warnings!")
                    self.ok_cells.append(current_cell)
            else:
                print("Adriane DEBUG check OK!")
                self.ok_cells.append(current_cell)
