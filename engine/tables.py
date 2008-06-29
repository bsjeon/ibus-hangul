# vim:set noet ts=4:
# -*- coding: utf-8 -*-
#
# ibus-anthy - The Anthy engine for IBus
#
# Copyright (c) 2007-2008 Huang Peng <shawn.p.huang@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

# string, result, cont
romaji_typing_rule = {
    u"-" : u"ー",
    u"a" : u"あ",
    u"i" : u"い",
    u"u" : u"う",
    u"e" : u"え",
    u"o" : u"お",
    u"xa" : u"ぁ",
    u"xi" : u"ぃ",
    u"xu" : u"ぅ",
    u"xe" : u"ぇ",
    u"xo" : u"ぉ",
    u"la" : u"ぁ",
    u"li" : u"ぃ",
    u"lu" : u"ぅ",
    u"le" : u"ぇ",
    u"lo" : u"ぉ",
    u"wi" : u"うぃ",
    u"we" : u"うぇ",
    u"wha" : u"うぁ",
    u"whi" : u"うぃ",
    u"whe" : u"うぇ",
    u"who" : u"うぉ",
    u"va" : u"ヴぁ",
    u"vi" : u"ヴぃ",
    u"vu" : u"ヴ",
    u"ve" : u"ヴぇ",
    u"vo" : u"ヴぉ",
    u"ka" : u"か",
    u"ki" : u"き",
    u"ku" : u"く",
    u"ke" : u"け",
    u"ko" : u"こ",
    u"ga" : u"が",
    u"gi" : u"ぎ",
    u"gu" : u"ぐ",
    u"ge" : u"げ",
    u"go" : u"ご",
    u"kya" : u"きゃ",
    u"kyi" : u"きぃ",
    u"kyu" : u"きゅ",
    u"kye" : u"きぇ",
    u"kyo" : u"きょ",
    u"gya" : u"ぎゃ",
    u"gyi" : u"ぎぃ",
    u"gyu" : u"ぎゅ",
    u"gye" : u"ぎぇ",
    u"gyo" : u"ぎょ",
    u"sa" : u"さ",
    u"si" : u"し",
    u"su" : u"す",
    u"se" : u"せ",
    u"so" : u"そ",
    u"za" : u"ざ",
    u"zi" : u"じ",
    u"zu" : u"ず",
    u"ze" : u"ぜ",
    u"zo" : u"ぞ",
    u"sya" : u"しゃ",
    u"syi" : u"しぃ",
    u"syu" : u"しゅ",
    u"sye" : u"しぇ",
    u"syo" : u"しょ",
    u"sha" : u"しゃ",
    u"shi" : u"し",
    u"shu" : u"しゅ",
    u"she" : u"しぇ",
    u"sho" : u"しょ",
    u"zya" : u"じゃ",
    u"zyi" : u"じぃ",
    u"zyu" : u"じゅ",
    u"zye" : u"じぇ",
    u"zyo" : u"じょ",
    u"ja" : u"じゃ",
    u"jya" : u"じゃ",
    u"ji" : u"じ",
    u"jyi" : u"じぃ",
    u"ju" : u"じゅ",
    u"jyu" : u"じゅ",
    u"je" : u"じぇ",
    u"jye" : u"じぇ",
    u"jo" : u"じょ",
    u"jyo" : u"じょ",
    u"ta" : u"た",
    u"ti" : u"ち",
    u"tu" : u"つ",
    u"tsu" : u"つ",
    u"te" : u"て",
    u"to" : u"と",
    u"da" : u"だ",
    u"di" : u"ぢ",
    u"du" : u"づ",
    u"de" : u"で",
    u"do" : u"ど",
    u"xtu" : u"っ",
    u"xtsu" : u"っ",
    u"ltu" : u"っ",
    u"ltsu" : u"っ",
    u"tya" : u"ちゃ",
    u"tyi" : u"ちぃ",
    u"tyu" : u"ちゅ",
    u"tye" : u"ちぇ",
    u"tyo" : u"ちょ",
    u"cha" : u"ちゃ",
    u"chi" : u"ち",
    u"chu" : u"ちゅ",
    u"che" : u"ちぇ",
    u"cho" : u"ちょ",
    u"dya" : u"ぢゃ",
    u"dyi" : u"ぢぃ",
    u"dyu" : u"ぢゅ",
    u"dye" : u"ぢぇ",
    u"dyo" : u"ぢょ",
    u"tha" : u"てゃ",
    u"thi" : u"てぃ",
    u"thu" : u"てゅ",
    u"the" : u"てぇ",
    u"tho" : u"てょ",
    u"dha" : u"でゃ",
    u"dhi" : u"でぃ",
    u"dhu" : u"でゅ",
    u"dhe" : u"でぇ",
    u"dho" : u"でょ",
    u"na" : u"な",
    u"ni" : u"に",
    u"nu" : u"ぬ",
    u"ne" : u"ね",
    u"no" : u"の",
    u"nya" : u"にゃ",
    u"nyi" : u"にぃ",
    u"nyu" : u"にゅ",
    u"nye" : u"にぇ",
    u"nyo" : u"にょ",
    u"ha" : u"は",
    u"hi" : u"ひ",
    u"hu" : u"ふ",
    u"fu" : u"ふ",
    u"he" : u"へ",
    u"ho" : u"ほ",
    u"ba" : u"ば",
    u"bi" : u"び",
    u"bu" : u"ぶ",
    u"be" : u"べ",
    u"bo" : u"ぼ",
    u"pa" : u"ぱ",
    u"pi" : u"ぴ",
    u"pu" : u"ぷ",
    u"pe" : u"ぺ",
    u"po" : u"ぽ",
    u"hya" : u"ひゃ",
    u"hyi" : u"ひぃ",
    u"hyu" : u"ひゅ",
    u"hye" : u"ひぇ",
    u"hyo" : u"ひょ",
    u"bya" : u"びゃ",
    u"byi" : u"びぃ",
    u"byu" : u"びゅ",
    u"bye" : u"びぇ",
    u"byo" : u"びょ",
    u"pya" : u"ぴゃ",
    u"pyi" : u"ぴぃ",
    u"pyu" : u"ぴゅ",
    u"pye" : u"ぴぇ",
    u"pyo" : u"ぴょ",
    u"fa" : u"ふぁ",
    u"fi" : u"ふぃ",
    u"fu" : u"ふ",
    u"fe" : u"ふぇ",
    u"fo" : u"ふぉ",
    u"ma" : u"ま",
    u"mi" : u"み",
    u"mu" : u"む",
    u"me" : u"め",
    u"mo" : u"も",
    u"mya" : u"みゃ",
    u"myi" : u"みぃ",
    u"myu" : u"みゅ",
    u"mye" : u"みぇ",
    u"myo" : u"みょ",
    u"lya" : u"ゃ",
    u"xya" : u"ゃ",
    u"ya" : u"や",
    u"lyu" : u"ゅ",
    u"xyu" : u"ゅ",
    u"yu" : u"ゆ",
    u"lyo" : u"ょ",
    u"xyo" : u"ょ",
    u"yo" : u"よ",
    u"ra" : u"ら",
    u"ri" : u"り",
    u"ru" : u"る",
    u"re" : u"れ",
    u"ro" : u"ろ",
    u"rya" : u"りゃ",
    u"ryi" : u"りぃ",
    u"ryu" : u"りゅ",
    u"rye" : u"りぇ",
    u"ryo" : u"りょ",
    u"xwa" : u"ゎ",
    u"wa" : u"わ",
    u"wo" : u"を",
# u"n'" : u"ん",
    u"nn" : u"ん",
    u"wyi" : u"ゐ",
    u"wye" : u"ゑ",
}

#hiragana, katakana, half_katakana
hiragana_katakana_table = { 
    u"あ" : (u"ア", u"ｱ"),
    u"い" : (u"イ", u"ｲ"),
    u"う" : (u"ウ", u"ｳ"),
    u"え" : (u"エ", u"ｴ"),
    u"お" : (u"オ", u"ｵ"),
    u"か" : (u"カ", u"ｶ"),
    u"き" : (u"キ", u"ｷ"),
    u"く" : (u"ク", u"ｸ"),
    u"け" : (u"ケ", u"ｹ"),
    u"こ" : (u"コ", u"ｺ"),
    u"が" : (u"ガ", u"ｶﾞ"),
    u"ぎ" : (u"ギ", u"ｷﾞ"),
    u"ぐ" : (u"グ", u"ｸﾞ"),
    u"げ" : (u"ゲ", u"ｹﾞ"),
    u"ご" : (u"ゴ", u"ｺﾞ"),
    u"さ" : (u"サ", u"ｻ"),
    u"し" : (u"シ", u"ｼ"),
    u"す" : (u"ス", u"ｽ"),
    u"せ" : (u"セ", u"ｾ"),
    u"そ" : (u"ソ", u"ｿ"),
    u"ざ" : (u"ザ", u"ｻﾞ"),
    u"じ" : (u"ジ", u"ｼﾞ"),
    u"ず" : (u"ズ", u"ｽﾞ"),
    u"ぜ" : (u"ゼ", u"ｾﾞ"),
    u"ぞ" : (u"ゾ", u"ｿﾞ"),
    u"た" : (u"タ", u"ﾀ"),
    u"ち" : (u"チ", u"ﾁ"),
    u"つ" : (u"ツ", u"ﾂ"),
    u"て" : (u"テ", u"ﾃ"),
    u"と" : (u"ト", u"ﾄ"),
    u"だ" : (u"ダ", u"ﾀﾞ"),
    u"ぢ" : (u"ヂ", u"ﾁﾞ"),
    u"づ" : (u"ヅ", u"ﾂﾞ"),
    u"で" : (u"デ", u"ﾃﾞ"),
    u"ど" : (u"ド", u"ﾄﾞ"),
    u"な" : (u"ナ", u"ﾅ"),
    u"に" : (u"ニ", u"ﾆ"),
    u"ぬ" : (u"ヌ", u"ﾇ"),
    u"ね" : (u"ネ", u"ﾈ"),
    u"の" : (u"ノ", u"ﾉ"),
    u"は" : (u"ハ", u"ﾊ"),
    u"ひ" : (u"ヒ", u"ﾋ"),
    u"ふ" : (u"フ", u"ﾌ"),
    u"へ" : (u"ヘ", u"ﾍ"),
    u"ほ" : (u"ホ", u"ﾎ"),
    u"ば" : (u"バ", u"ﾊﾞ"),
    u"び" : (u"ビ", u"ﾋﾞ"),
    u"ぶ" : (u"ブ", u"ﾌﾞ"),
    u"べ" : (u"ベ", u"ﾍﾞ"),
    u"ぼ" : (u"ボ", u"ﾎﾞ"),
    u"ぱ" : (u"パ", u"ﾊﾟ"),
    u"ぴ" : (u"ピ", u"ﾋﾟ"),
    u"ぷ" : (u"プ", u"ﾌﾟ"),
    u"ぺ" : (u"ペ", u"ﾍﾟ"),
    u"ぽ" : (u"ポ", u"ﾎﾟ"),
    u"ま" : (u"マ", u"ﾏ"),
    u"み" : (u"ミ", u"ﾐ"),
    u"む" : (u"ム", u"ﾑ"),
    u"め" : (u"メ", u"ﾒ"),
    u"も" : (u"モ", u"ﾓ"),
    u"や" : (u"ヤ", u"ﾔ"),
    u"ゆ" : (u"ユ", u"ﾕ"),
    u"よ" : (u"ヨ", u"ﾖ"),
    u"ら" : (u"ラ", u"ﾗ"),
    u"り" : (u"リ", u"ﾘ"),
    u"る" : (u"ル", u"ﾙ"),
    u"れ" : (u"レ", u"ﾚ"),
    u"ろ" : (u"ロ", u"ﾛ"),
    u"わ" : (u"ワ", u"ﾜ"),
    u"を" : (u"ヲ", u"ｦ"),
    u"ん" : (u"ン", u"ﾝ"),
    u"ぁ" : (u"ァ", u"ｧ"),
    u"ぃ" : (u"ィ", u"ｨ"),
    u"ぅ" : (u"ゥ", u"ｩ"),
    u"ぇ" : (u"ェ", u"ｪ"),
    u"ぉ" : (u"ォ", u"ｫ"),
    u"っ" : (u"ッ", u"ｯ"),
    u"ゃ" : (u"ャ", u"ｬ"),
    u"ゅ" : (u"ュ", u"ｭ"),
    u"ょ" : (u"ョ", u"ｮ"),
    u"ヵ" : (u"ヵ", u"ｶ"),
    u"ヶ" : (u"ヶ", u"ｹ"),
    u"ゎ" : (u"ヮ", u"ﾜ"),
    u"ゐ" : (u"ヰ", u"ｨ"),
    u"ゑ" : (u"ヱ", u"ｪ"),
    u"ヴ" : (u"ヴ", u"ｳﾞ"),
    u"ー" : (u"ー", u"ｰ"),
    u"、" : (u"、", u"､"),
    u"。" : (u"。", u"｡"),
    u"！" : (u"！", u"!"),
    u"”" : (u"”", u"\""),
    u"＃" : (u"＃", u"#"),
    u"＄" : (u"＄", u"$"),
    u"％" : (u"％", u"%"),
    u"＆" : (u"＆", u"&"),
    u"’" : (u"’", u"'"),
    u"（" : (u"（", u""),
    u"）" : (u"）", u")"),
    u"〜" : (u"〜", u"~"),
    u"＝" : (u"＝", u"="),
    u"＾" : (u"＾", u"u"),
    u"＼" : (u"＼", u"\\"),
    u"｜" : (u"｜", u"|"),
    u"‘" : (u"‘", u"`"),
    u"＠" : (u"＠", u"@"),
    u"｛" : (u"｛", u""),
    u"「" : (u"「", u"｢"),
    u"＋" : (u"＋", u"+"),
    u"；" : (u"；", u";"),
    u"＊" : (u"＊", u"*"),
    u"：" : (u"：", u" : u"),
    u"｝" : (u"｝", u")"),
    u"」" : (u"」", u"｣"),
    u"＜" : (u"＜", u"<"),
    u"＞" : (u"＞", u">"),
    u"？" : (u"？", u"?"),
    u"／" : (u"／", u"/"),
    u"＿" : (u"＿", u"_"),
}
