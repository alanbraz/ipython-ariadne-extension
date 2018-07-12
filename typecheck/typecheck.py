class TypeCheck(object):

    def __init__(self, ip):
        self.shell = ip
        self.ok_cells = [ "import os", "os.environ['MYPYPATH'] = os.environ['PYTHONPATH']" ]
        ip.run_cell("\n".join(self.ok_cells))

    def check(self):
        # print("typecheck...")
        from mypy import api
        import sys
        cells = self.shell.user_ns["In"]
        # print("cells", cells)
        current_cell = cells[-1]
        # print("current_cell", current_cell)
        current_cell_lines = []
        for line in current_cell.split("\n"):
            # ignore magic commands
            if "get_ipython" not in line:
                current_cell_lines.append(line)
        if len(current_cell_lines) > 0:
            current_cell = "\n".join(current_cell_lines)
            cells_to_run = "\n".join(self.ok_cells + [current_cell])
            # print("cells_to_run", cells_to_run)
            mypy_result = api.run(['-c', cells_to_run, '--ignore-missing-imports', '--show-column-numbers'])
            error = None
            if mypy_result[0]:
                error = mypy_result[0]
            if mypy_result[1]:
                error = mypy_result[1]
            if error is not None:
                parts = error.split(":")
                error_line_number = int(parts[1])
                error_column_number = int(parts[2])
                error_line_number = error_line_number - len(("\n".join(self.ok_cells)).split("\n"))
                
                line_label = "Line "+ str(error_line_number) + ": "
                error_message = "TypeCheck" + parts[3] + ":" + parts[4]
                error_message = error_message + "\n" + line_label + current_cell_lines[error_line_number-1]
                error_message = error_message + "\n" + len(line_label)*" "+ (error_column_number-1)*" " + "^"
                print(error_message, file=sys.stderr)
            else:
                self.ok_cells.append(current_cell)
