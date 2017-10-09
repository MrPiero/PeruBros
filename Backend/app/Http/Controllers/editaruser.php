<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\User;


class editaruser extends Controller
{
    //
    public function index(Request $request){


    }
    public function editar(Request $request){

    $id=$request->id_user;
    $usuario=User::find($id);

        $usuario->email=$request->email;
        $usuario->name=$request->nombre;
        $usuario->password=bcrypt($request->password_nuevo);
        $usuario->save();
        return back()
            ->with('success','Se ha modificado el usuario Correctamente');


    }

    public function crearPersonaje(Request $request){

    }

}
