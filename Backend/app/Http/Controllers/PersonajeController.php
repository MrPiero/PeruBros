<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Personaje;

class PersonajeController extends Controller
{
    //


    public function add(Request $request){
        $personaje=new Personaje();
        $personaje->nombre=$request->nombre;
        $personaje->sexo=$request->sexo;
        $personaje->id_usuario= $request->id_user;


        return back('succes','Se Agrego el Personaje Correctamente');
    }
}
