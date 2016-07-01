import os,sys,re
import shutil, errno
if __name__ == "__main__":
        if len(sys.argv) == 2:
                arg = sys.argv[1]
                if arg == "dist":
                        """
                        Create the directory of distribution and
                        copy all files of development directory to him.
                        """
                        path = os.path.dirname(os.path.realpath(__file__))
                        file = "/libpfp/src/src_build/setup.py"
                        path_file = "%s%s"%(path,file)
                        f = open(path_file)
                        content = f.read()
                        f.close()
                        major_result = re.search('MAJOR[\s]+=(.*)',content)
                        minor_result = re.search('MINOR[\s]+=(.*)',content)
                        micro_result = re.search('MICRO[\s]+=(.*)',content)
                        if major_result != None and minor_result != None and micro_result != None:
                                MAJOR = major_result.group(1)
                                MINOR = minor_result.group(1)
                                MICRO = micro_result.group(1)
                                VERSION = MAJOR.strip()+"."+MINOR.strip()+"."+MICRO.strip() 
                                dir_name = "%s/LibPFP-%s"%(path,VERSION)
                                dir_only_name = "LibPFP-%s"%(VERSION)
                                try:
                                        shutil.rmtree(dir_name)
                                except OSError,oe:
                                        pass                                        
                                origem = "%s/libpfp/"%(path)
                                destino = "%s/"%(dir_name)
                                try:
                                        shutil.copytree(origem, destino)
                                except OSError,oe: # python >2.5
                                        if oe.errno == errno.ENOTDIR:
                                                shutil.copy(origem, destino)
                                        else: raise
                        
                        """
                        Delete git files
                        """                        
                        git_dir = "%s/.git/"%(dir_name)
                        git_file = "%s/.gitignore"%(dir_name)
                        try:
                                shutil.rmtree(git_dir)
                        except OSError,oe:
                                print "Nao foi possivel remover o diretorio .git/, provavelmente ele nao existe."
                                pass
                        try:
                                os.remove(git_file)
                        except OSError,oe:
                                print "Nao foi possivel remover o arquivo .gitignore, provavelmente ele nao existe."
                                pass
                        
                        """
                        Compact file to distribute
                        """
                        import tarfile
                        try:
                                tar = tarfile.open(dir_only_name+".tar.gz", "w:gz")
                                tar.add(dir_only_name+"/")
                                tar.close()
                        except Exception as e:
                                print e