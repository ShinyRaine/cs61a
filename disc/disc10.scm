; Write a function that returns the factorial of a number.
(define (factorial x) 
  (if (= x 1)
    1
    (* x (factorial (- x 1)))
  )
)

; Write a function that returns the nth Fibonacci number
(define (fib n)
  (if (= n 0)
  0
  (if (= n 1)
  1
  (+ (fib (- n 1)) (fib (- n 2)))
  )
  )
)

; Write a function which takes two lists and concatenates them
(define (my-append a b)
  (if (eq? a nil)
  b
  (cons (car a) (my-append 
  (cdr a)
  b
  ))
  )
)
(my-append '(1 2 3) '(2 3 4))

;Write a Scheme function that, when given an element, a list, and an index, insertsthe element into the list at that index.
(define (insert element lst index)
  (if (= 0 index)
  (cons element lst)
  (cons (car lst) (insert element (cdr lst) (- index 1)))
  )
)

; Write a Scheme function that, when given a list, such as (1 2 3 4), duplicates
; every element in the list (i.e. (1 1 2 2 3 3 4 4)).
(define (duplicate lst)
  (if (eq? lst nil)
  '()
  (cons (car lst) (cons (car lst) (duplicate (cdr lst))))
  )
)