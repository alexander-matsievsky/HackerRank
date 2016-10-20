{-# LANGUAGE TemplateHaskell #-}
module FunctionalProgrammingWarmupsInRecursionGcd(runTests) where
import           Test.QuickCheck
import           Test.QuickCheck.All
import           Debug.Trace

main :: IO ()
main = interact run

run :: String -> String
run input = output where
    [a, b] = map (read::String -> Integer) . words $ input
    output = show $ gcd' a b

gcd' :: (Ord t, Num t) => t -> t -> t
gcd' x y
    | y == 0 = x
    | x == 0 = y
    | otherwise = gcd' (x' - y') y' where x' = max x y; y' = min x y

prop_run = run "1 5" == "1"
prop_run1 = run "10 100" == "10"
prop_run2 = run "22 131" == "1"
prop_run3 (NonNegative a) (NonNegative b) = gcd' a b == gcd a b

return []
runTests = $quickCheckAll
