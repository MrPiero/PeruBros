
<!DOCTYPE HTML>
<!--
Prologue by HTML5 UP
	html5up.net | @ajlkn
Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
-->
<html>
<head>
    <title>PeruBross</title>
    <meta charset="utf-8" />
    <!-- CSRF Token -->
    <meta name="csrf-token" content="{{ csrf_token() }}">

    <link href="{{ asset('css/app.css') }}" rel="stylesheet">


    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <!--[if lte IE 8]>
    <script src="../../../../../Downloads/html5up-prologue/assets/js/ie/html5shiv.js"></script><![endif]-->
    <link rel="stylesheet" href="css/main.css" />
    <!--[if lte IE 8]>
    <link rel="stylesheet" href="css/ie8.css"/><![endif]-->
    <!--[if lte IE 9]>
    <link rel="stylesheet" href="css/ie9.css"/><![endif]-->


    <link rel="stylesheet" href="css/skeleton.css"/><![endif]-->
    <!--[if lte IE 9]>
    <link rel="stylesheet" href="css/normalize.css"/><![endif]-->

    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous"/>

</head>
<body>

<!-- Header -->
<div id="header">

    <div class="top">

        <!-- Logo -->
        <div id="logo">
            <span class="image avatar48"><img src="/images/avatar.jpg" alt="" /></span>
            <h1 id="title">{{ Auth::user()->name }}</h1>

        </div>

        <!-- Nav -->
        <nav id="nav">

            <ul>
                <li><a href="#top" id="top-link" class="skel-layers-ignoreHref"><span class="icon fa-home">Descarga</span></a></li>
                <li><a href="#portfolio" id="portfolio-link" class="skel-layers-ignoreHref"><span class="icon fa-th">Perfil</span></a></li>
                <li><a href="#about" id="about-link" class="skel-layers-ignoreHref"><span class="icon fa-user">Personaje</span></a></li>
                <li><a href="#contact" id="contact-link" class="skel-layers-ignoreHref"><span class="icon fa-envelope">Logros</span></a></li>
            </ul>
        </nav>

    </div>

    <div class="bottom">

        <!-- Social Icons -->
        <ul class="icons">
            <li><a href="#" class="icon fa-twitter"><span class="label">Twitter</span></a></li>
            <li><a href="#" class="icon fa-facebook"><span class="label">Facebook</span></a></li>
            <li><a href="#" class="icon fa-github"><span class="label">Github</span></a></li>
            <li><a href="#" class="icon fa-dribbble"><span class="label">Dribbble</span></a></li>
            <li><a href="#" class="icon fa-envelope"><span class="label">Email</span></a></li>
        </ul>

    </div>

</div>

<!-- Main -->
<div id="main">

    <!-- Intro -->
    <section id="top" class="one dark cover">
        <div class="container">
            @if ($message = Session::get('success'))
                <div class="alert alert-success alert-block">
                    <button type="button" class="close" data-dismiss="alert">×</button>
                    <strong>{{ $message }}</strong>
                </div>
            @endif
            <header>
                <h2 class="alt">Hola Bienvenido a <strong>PeruBross</strong>, el mejor juego de aventura antes creado!, si estas listo para empezar la aventura
                descarga el juego aqui </h2>

            </header>

            <footer>
                <a href="#portfolio" class="button scrolly">Descarga PeruBross</a>
            </footer>

        </div>
    </section>

    <!-- Portfolio -->
    <section id="portfolio" class="two">
        <div class="container">

            <header>
                <h2>Editar Perfil</h2>
            </header>


            <!-- The above form looks like this -->
            <form action="{{ url('/usuarioeditar') }}" method="post">
                {{ csrf_field() }}
                <div class="row">
                    <div class="six columns">
                        <label for="exampleEmailInput">Correo</label>
                        <input class="u-full-width" type="email" name="email" value="{{ Auth::user()->email }}">
                    </div>
                    <div class="six columns">
                        <label for="exampleEmailInput">Nombre</label>
                        <input class="u-full-width" type="text"  name="nombre" value="{{ Auth::user()->name }}">
                    </div>

                    {{--<div class="six columns" style="padding: 0 0 0 0;">--}}
                        {{--<label for="exampleEmailInput">Password Antiguo</label>--}}
                        {{--<input class="u-full-width" type="password" name="password_antiguo" >--}}
                    {{--</div>--}}
                    <div class="six columns" style="padding: 0 0 0 0;">
                        <label for="exampleEmailInput">Password Nuevo</label>
                        <input class="u-full-width" type="password" name="password_nuevo">
                    </div>


                </div>

                <input type="hidden" id="id_user" name="id_user" value="{{Auth::user()->id}}"/>
                <input class="button-primary" type="submit" value="Actualizar">
            </form>

        </div>
    </section>

    <!-- About Me -->
    <section id="about" class="three">
        <div class="container">

            <header>
                <h2>Personaje</h2>
            </header>

            <a href="#" class="image featured"><img src="/images/pic08.jpg" alt="" /></a>

            <p>Recuerda que para modificar los personajes del juego tienes que hacer por la web!</p>




                <!-- Button to trigger modal -->

                <button class="btn btn-info" data-toggle="modal" data-target="#viewModal" >Agregar Personaje</button>

            <div class="modal fade" id="viewModal" role="dialog">
                <div class="modal-dialog">

                    <div class="modal-content">
                        <div class="modal-header">
                            <button type="button" class="close" data-dismiss="modal">&times;</button>
                            <h4 class="modal-title">Agregar Personaje</h4>
                        </div>
                        <div class="modal-body">

                            <form>
                                <div class="form-group">
                                    <label for="personajenombre">Nombre del Personaje</label>
                                    <input type="email" class="form-control" id="personajenombre"  placeholder="Ingresa el Personaje" name="personaje_name">

                                </div>
                                <div class="form-group">
                                    <label for="personajesexo">Elige tu Personaje</label>






                                    <div class="five columns" style="padding: 0 0 0 0;">
                                        <figure class="prueba1"><img src="https://cdn.pixabay.com/user/2017/03/20/11-03-17-367_250x250.jpg" class="imagencompra" id="hombre" /></figure>

                                    </div>
                                    <div class="five columns" style="padding: 0 0 0 0;">
                                        <figure class="prueba1"><img src="https://cdn.pixabay.com/user/2017/03/20/11-03-17-367_250x250.jpg" class="imagencompra" id="mujer" /></figure>

                                    </div>


                                </div>

                                <button type="submit" class="btn btn-primary">Submit</button>
                            </form>


                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                        </div>

                    </div>

                </div>
            </div>



            </div>

    </section>

    <!-- Contact -->
    <section id="contact" class="four">
        <div class="container">



        </div>
    </section>

</div>

<!-- Footer -->
<div id="footer">

    <!-- Copyright -->
    <ul class="copyright">
        <li>&copy; PeruBross</li>
    </ul>

</div>

<!-- Scripts -->
<script src="js/jquery.min.js"></script>
<script src="js/jquery.scrolly.min.js"></script>
<script src="js/jquery.scrollzer.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
<script src="js/skel.min.js"></script>
<script src="js/util.js"></script>
<!--[if lte IE 8]>
<script src="js/ie/respond.min.js"></script><![endif]-->
<script src="js/main.js"></script>



<script>


    $('.imagencompra').click(function(){

        $('.selected').removeClass('selected'); // removes the previous selected class
        $(this).addClass('selected'); // adds the class to the clicked image
        //alert(this.id);
    });



</script>
</body>
</html>