main = do
    let y = 5
    let x = square y
    let z = doubleNums x y

    let d = function x y z
    print(d)

    print(lotto d)
    print(smallDouble d)

    print(check 2)
    
    print(13+4-1/2) -- plus minus dividieren
    print((+) 16 26) -- in order polish notation
    print(6 `div` 5) -- integer division
    print(4 <= 4) -- comparison
    print(4 /= 5) -- check for unequality
    print(rem 4 2) -- remainder operation
    print(rem 4 3) -- remainder operation
    print(mod 4 3) -- modulo operation
    print(2**1023) -- power of
    print(2**1024) -- infinity
    print(2^256)   -- power of
    print(map (*2) [1, 2, 3]) -- maps values
    print(filter (>5) [8, 4, 1, 6, 10]) -- filers larger than 5
    print(cos 0) -- cos
    print(sin pi) -- sin
    print('3' < 'a') -- checks if ascii value is larger
    print('a' < '3') -- check ascii values
    print("who" < "z") -- check ascii values from first index 
    print(sqrt 3) -- squareroot
    print(abs (-9)) -- returns absolute value
    print(rem 5 (-2)) -- remainder with negative number
    print(mod 5 (-2))
    print(div 4 5)
    print(rem (-5) (-2))
    print(mod (-5) 2)
    print('a'<'0')
    print('a' > '0')
    print("Hallo")

    print(checkEven 9)
    print(summation 100)
    print(mersenne(summation 100))
    print(order 5 3 1)
    print(windchill 10 2)
    print(strange 10)
    print([x*2 | x <- [1..20]])
    print([x | x <- [1..10], odd x])
    print([x*2 | x <- [1..10], x*2 >= 15])
    print([ x | x <- [50..100], x `mod` 7 == 3])
    print(superToll [5..13])
    print(laenge [2, 7, 3, 9])

    let kombis = [ (a,b,c) | c <- [1..3], b <- [1..3], a <- [1..3] ]
    print(kombis)
    let kombis2 = [ (a,b,c) | c <- [1..3], b <- [1..c], a <- [1..b] ]
    print(kombis2)
    let besondere = [ (a,b,c) | c <- [1..10], b <- [1..c], a <- [1..b], a^2 + b^2 == c^2]
    print(besondere!!0)
    print(triangle 1 2 3)

    print(bmi 63 1.85)

    print(checkBracket 'a')

    print(sod 1234)

    print(fib 5)
square :: Int -> Int
square y = y*y

doubleNums :: Int -> Int -> Int
doubleNums x y = x*2 + y*2

function :: Int -> Int -> Int -> Int
function x y z = x*y + x*z

lotto :: Int -> Bool
lotto x = x == 7

smallDouble :: Int -> Int
smallDouble x = if x > 50
    then x*2
    else x

check :: Int -> Char
check a = case a of
    1 -> 'A'
    2 -> 'B'
    otherwise -> error "Wrong number"

checkEven :: Int -> Bool
checkEven a = mod a 2 == 0

summation :: Int -> Int
summation b = b*(b+1) `div` 2

mersenne :: Int -> Int
mersenne c = 2*c-1

order :: Int -> Int -> Int -> [Char]
order a b c = if a < b
    then if b < c
        then "Increasing Order"
        else error "Number is invalid"
    else if b > c
        then "Decreasing Order"
        else error "Number is invalid"

-- windchill :: Int -> Int -> Float

windchill t v = 13.12+0.6215*t-11.37*v**0.16+0.3965*t*v**0.16

strange :: Int -> Int
strange x
    | x > 10 = div (x+3) 2
    | x < 10 = (div (x*x) 3) +5
    | otherwise = square x

superToll xs = [ if x < 10 then "Super!" else "Toll!" | x <- xs, odd x]

laenge xs = sum [1 | _ <- xs]

triangle a b c = if abs(a)+abs(b) >= abs(a+b)
    then True
    else False

checkBracket a = if a =='('||a==')'||a=='['||a==']'||a=='{'||a=='}'
    then True
    else False

bmi k g = 
    -- let i = k/g**2
    if k/g**2 < 18
        then "Untergewichtig"
    else if k/g**2 > 25
        then "Übergewichtig"
    else "Normal"

sod d
    | d<10 =d
    | d >= 10 = d `mod` 10 + sod(d `div` 10)