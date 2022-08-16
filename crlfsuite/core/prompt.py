import os
import tempfile

def prompt():
    """
    Opens a temporary file in nano editor and returns the content that user pasted 
    """
    editor = 'nano'
    with tempfile.NamedTemporaryFile(mode='r+') as tmpfile:
        child_pid = os.fork()
        is_child = child_pid == 0
        if is_child:
            os.execvp(editor, [editor, tmpfile.name])
        else:
            os.waitpid(child_pid, 0)
            tmpfile.seek(0)
            return tmpfile.read().strip()