import os, tempfile

class PythonListener:
    
    def __init__(self):
        #outpath = os.path.join(tempfile.gettempdir(), 'listen.txt')
        self.outfile = open('li.txt', 'w')
        
    def start_suite(self, name, doc):
        self.outfile.write("%s '%s'\n" % (name, doc))
        
    def start_test(self, name, doc, tags):
        self.outfile.write("- %s '%s' [ %s ] :: " % (name, doc, ' '.join(tags)))
        
    def end_test(self, status, message):
        if status == 'PASS':
            self.outfile.write('PASS\n')
        else:
            self.outfile.write('%s: %s\n' % (status, message))
            
    def end_suite(self, status, message):
        self.outfile.write('%s\n%s\n' % (status, message))
            
    def close(self):
        self.outfile.close()
