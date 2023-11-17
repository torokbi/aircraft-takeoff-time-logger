setInterval(auto_update,1000*60);


function auto_update()
{
    
    var req = new XMLHttpRequest();
    req.onreadystatechange = function()
    {
        if(this.readyState == 4 && this.status == 200)
        {
            var planes = JSON.parse(this.responseText);

            for (var plane of planes)
            {
                document.getElementById(plane.registracion + "-before").innerText = plane.beforetime + " perc";

                
                if(plane.beforetime == 0){
                    try
                    {
                        var planerow = document.getElementById(plane.registracion + "-trow");
                        var planetakeoffdiv = document.getElementById(plane.registracion + "-takeoffdiv");

                        if("table-success" in planerow.classList) continue;
                        
                        var planewarningmessagebox = document.getElementById("retakeoff" + plane.registracion);
                        planewarningmessagebox.remove();

                        var takeoffbutton = document.createElement('a');
                        var link = document.createTextNode("Felszállás");
                        takeoffbutton.appendChild(link);
                        takeoffbutton.href = "/retakeoff/" + plane.id;
                        takeoffbutton.classList.add("btn");
                        takeoffbutton.classList.add("btn-warning");


                        planerow.classList.add("table-success");
                        planerow.classList.remove("table-warning");
                        planetakeoffdiv.replaceChild(takeoffbutton, planetakeoffdiv.childNodes[1]);
                        console.log(plane.registracion + " sikeresen frissítve")
                    }
                    catch(e)
                    {
                        console.log(e);
                    }
                }
                else
                {
                    var planerow = document.getElementById(plane.registracion + "-trow");
                    console.log(planerow.classList);
                }
            }
        }
    }

    req.open('GET', '/_getplanes', true);
    req.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
    req.send("name=" + "auto_updater");
}