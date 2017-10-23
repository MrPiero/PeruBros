# Este archivo esta encargado de inicializar la aplicacion

from bin import main
import sys

if len(sys.argv) == 1:
    main.main()
elif sys.argv[1] == 'test':
    main.test()