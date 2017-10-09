<?php

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', function () {
    return view('welcome');
});

Auth::routes();


Route::get('/logout', function(){
    Session::flush();
    Auth::logout();
    return Redirect::to("/cuenta")
        ->with('message', 'Tu session ha sido cerrada con exito!');
});
Route::get('/cuenta', 'HomeController@index')->name('home');
Route::get('/usuario', 'editaruser@index');
Route::post('/usuarioeditar', 'editaruser@editar');
