using IronPython.Hosting;
using Microsoft.Scripting.Hosting;

namespace BlazorApp1.Data
{
     public class File_manager
    {
        ScriptEngine engine = Python.CreateEngine();
        public File_manager()
        {
            engine.ExecuteFile("./Scripts/file_service.py");
        }
    }
    
}
