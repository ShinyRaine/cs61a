(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cdr (cdr s)))
)


(define (sign num)
  (cond
  ((> num 0) 1)
  ((= num 0) 0)
  (else (- 1))
  )
)


(define (square x) (* x x))

(define (pow x y)
  (if (= x 1)
  1
  (if (= y 0)
  1
  (* x (pow x (- y 1)))
  ))
)

(define (in v s)
  (cond
  ((eq? s '()) #f)
  ((eq? v (car s)) #t)
  (else (in v (cdr s)))
  )
)
(define (unique s)
  (define (helper s l)
    (cond 
      ((eq? s '()) l)
      ((in (car s) l) (helper (cdr s) l))
      (else (helper (cdr s) (append l (cons (car s) nil))))
    )
  )
  (helper s '())
)


(define (replicate x n)
  (define (helper n l)
  (if (= n 0)
  l
  (helper (- n 1) (cons x l))
  )
  )
  (helper n '())
)


(define (accumulate combiner start n term)
  (if (= n 0)
  start
  (accumulate combiner (combiner start (term n)) (- n 1) term)
  )
)


(define (accumulate-tail combiner start n term)
  (if (= n 0)
  start
  (accumulate combiner (combiner start (term n)) (- n 1) term)
  )
)


(define-macro (list-of map-expr for var in lst if filter-expr)
  (let ((l `(filter (lambda (,var) ,filter-expr) ,lst)))
  `(map (lambda (,var) ,map-expr) ,l))
)
