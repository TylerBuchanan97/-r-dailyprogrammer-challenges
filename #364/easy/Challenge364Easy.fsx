let input = ["5d12"; "6d4";"1d2"; "1d8"; "3d6"; "4d20"; "100d100"]

let rand = System.Random()

let randomInRange range =
    rand.Next(2, range + 1)

let roll times sides =
    let mutable value = 0
    for i in 1..times do 
        value <- value + randomInRange sides
    value

let parse =
    input
    |> List.map (fun str -> str.Split 'd')
    |> List.iter (fun x -> printfn "%d" (roll (x.[0] |> int) (x.[1] |> int)))