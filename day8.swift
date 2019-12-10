import Cocoa

let fileURL = Bundle.main.url(forResource: "day8", withExtension: "txt")
let content = try String(contentsOf: fileURL!, encoding: String.Encoding.utf8)

let input = content.compactMap { $0.wholeNumberValue }

let width = 25
let height = 6
let layerSize = width * height

let layers = stride(from: 0, to: input.count, by: layerSize).map {
    input[$0..<($0+layerSize)]
}

var stats: [(zeroes: Int, ones: Int, twoes: Int)] = []
for layer in layers {
    
    var counters = [Int](repeating: 0, count: 3)
    for pxl in layer {
        counters[pxl] += 1
    }
    stats.append((counters[0], counters[1], counters[2]))
}

stats.sort { lhs, rhs in
    return lhs.zeroes < rhs.zeroes
}

if let layer = stats.first {
    print("\(layer.ones * layer.twoes)")
}