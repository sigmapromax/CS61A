(define (over-or-under num1 num2) 
  (if (< num1 num2)
    -1
    (
      if (= num1 num2)
      0
      1
    )
  )
)

(define (make-adder num) 
    ( lambda (inc) (+ num inc) )
)

(define (composed f g)
    (lambda (x) (f (g x) ))
)

; (define lst (cons (cons 1 nil) 
;                   (cons 2 
;                         (cons (cons 3 (cons 4 nil))
;                               (cons 5 nil)))))
(define lst (list
                (list 1)
                2 
                (list 3 4) 
                5
            )
)

(define (remove item lst) 
        (cond ( (null? lst) '())
              ( (= item (car lst)) (remove item (cdr lst)))
              ( else (cons(car lst) (remove item (cdr lst))))
        )
)