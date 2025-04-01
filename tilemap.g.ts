// Auto-generated code. Do not edit.
namespace myTiles {
    //% fixedInstance jres blockIdentity=images._tile
    export const transparency16 = image.ofBuffer(hex``);

    helpers._registerFactory("tilemap", function(name: string) {
        switch(helpers.stringTrim(name)) {
            case "level1":
            case "level1":return tiles.createTilemap(hex`1000100001010101010101010101010101010101010606060d0d0d0d0d0d0d0207080501010606060d0d0d0d0d0d0d0305050501010d0d0d0d0d0d0d0d0d0d0305050501010d0d0d0d0d0d0d0d0d0d0305050501010d0d0d0d0d0d0d0d0d0d0405050501010d0d0d0d0d0d0d0d0d0d0d0a0a0a01010d0d0d0d0d0d0d0d0d0d0d0a0a0a01010d0d0d0d0d0d0d0d0d0d0d0a0a0a010109090909090d0d0d0d0d0d0a0a0a010105050505050c0c0c0c0c0c0b0a0a010105050505050c0c0c0c0c0c0c0b0a010105050505050c0c0c0c0c0c0c0c0b010105050505090d0d0d0d0d0d0d0d0d010105050505090d0d0d0d0d0d0d0d0d0101010101010101010101060101010101`, img`
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
. . . . . . . . . . . . . . . . 
`, [myTiles.transparency16,sprites.builtin.forestTiles0,sprites.dungeon.darkGroundNorthWest0,sprites.dungeon.darkGroundWest,sprites.dungeon.darkGroundSouthWest0,sprites.dungeon.darkGroundNorthWest1,sprites.dungeon.collectibleInsignia,sprites.dungeon.chestClosed,sprites.dungeon.collectibleRedCrystal,sprites.dungeon.darkGroundCenter,sprites.vehicle.roadVertical,sprites.vehicle.roadTurn4,sprites.vehicle.roadIntersection1,sprites.castle.tileDarkGrass2], TileScale.Sixteen);
        }
        return null;
    })

    helpers._registerFactory("tile", function(name: string) {
        switch(helpers.stringTrim(name)) {
            case "transparency16":return transparency16;
        }
        return null;
    })

}
// Auto-generated code. Do not edit.
