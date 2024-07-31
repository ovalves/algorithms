(defn find-median-sorted-arrays
     [nums-1 nums-2]
     (let [merged (flatten (conj nums-1 nums-2))
           len (count merged)
           median (quot len 2)]
          (if (= 0 (mod len 2))
               (float (/ (+ (nth (sort merged) median) (nth (sort merged) (dec median))) 2))
               (nth (sort merged) median))))

(println (find-median-sorted-arrays [1 3] [2])) ; 2 
(println (find-median-sorted-arrays [1 2] [3 4])) ; 2.5
(println (find-median-sorted-arrays [0 0] [0 0])) ; 0.0
(println (find-median-sorted-arrays [] [1])) ; 1
(println (find-median-sorted-arrays [2] [])) ; 2
