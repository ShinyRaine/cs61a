(define (rle s)
  (define (helper s p n)
  (cond
    ((null? s) (cons-stream (list p n) nil))
    ((eq? (car s) p) (helper (cdr-stream s) p (+ 1 n)))
    (else (cons-stream (list p n) (helper (cdr-stream s) (car s) 1)))
  ))
  (if (null? s)
  nil
  (helper (cdr-stream s) (car s) 1)
))


(define (group-by-nondecreasing s)
)


(define finite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 3
                (cons-stream 1
                    (cons-stream 2
                        (cons-stream 2
                            (cons-stream 1 nil))))))))

(define infinite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 2
                infinite-test-stream))))

