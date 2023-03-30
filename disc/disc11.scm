(define (reverse lst)
  (define (helper lst res)
    (if (null? lst)
    res
    (helper (cdr lst) (cons (car lst) res)))
  )
  (helper lst '())
)

(define (insert n lst)
  (define (helper lst res)
    (if (> (car lst) n)
    (append (reverse res) (cons n lst))
    (helper (cdr lst) (cons (car lst) res))
    )
  )
  (helper lst '())
)
(insert 6 '(2 4 5 7))

(define-macro (or-macro expr1 expr2)
`(let ((v1 ,expr1))
(if v1
  v1
  ,expr2
)))
(or-macro (print 'bork) (/ 1 0))

(define-macro (prune-expr expr)
)
(prune-expr (+ 10 100))

(define-macro (when condition exprs)
(list 'if condition (cons 'begin exprs) ''okay))

(define-macro (when condition exprs)
`(if ,condition (begin ,@exprs) 'okay))

(when (= 1 1) ((print 6) (print 1) 'a))