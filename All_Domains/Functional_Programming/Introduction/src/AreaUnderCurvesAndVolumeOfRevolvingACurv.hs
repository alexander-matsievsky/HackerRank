{-# LANGUAGE TemplateHaskell #-}
module AreaUnderCurvesAndVolumeOfRevolvingACurv(runTests) where
import           Test.QuickCheck
import           Test.QuickCheck.All
import           Text.Printf

main :: IO ()
main = interact run

run :: String -> String
run input = output where
    [as, bs, [l, r]] = map (map (read::String -> Double) . words) . lines $ input
    subInterval = 1E-3
    f x = sum [a * (x ** b) | (a, b) <- zip as bs]
    area = sum [f x * subInterval | x <- [l, l + subInterval .. r]]
    volume = sum [pi * (f x ** 2) * subInterval | x <- [l, l + subInterval .. r]]
    output = unlines . map (printf "%.1f") $ [area, volume]

prop_run = run "1 2 3 4 5\n\
\6 7 8 9 10\n\
\1 4  " == "2435300.3\n\
\26172951168899.3\n"

return []
runTests = $quickCheckAll
