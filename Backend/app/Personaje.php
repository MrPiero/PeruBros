<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Personaje extends Model
{
    //


    protected $fillable = [
        'id_usuario', 'nombre', 'sexo',
    ];


    public function user()
    {
        return $this->belongsTo('App\User');
    }
}
