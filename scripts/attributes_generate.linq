<Query Kind="Program">
  <Namespace>System.Linq</Namespace>
</Query>

void Main()
{
	var attributes = new Dictionary<string, string[]> {
		{ "Attributes", new string[] {
			"Strength",
			"Speed",
			"Fortitude",
			"Resolve",
			"Faith",
			"Intelligence"
		}},
		{ "Combat Skills", new string[] {
			"Archery",
			"Brawl",
			"Dodge",
			"Firearms",
			"Heavy Weapons",
			"Light Weapons",
			"Medium Weapons",
			"Parry",
			"Shields",
			"Steady"
		}},
		{ "Physical Skills", new string[] {
			"Finesse",
			"Grit",
			"Stealth",
			"Mobility"
		}},
		{ "Professional Skills", new string[] {
			"Mercantile",
			"Farming",
			"Forestry",
			"Herbalism",
			"Mining",
			"Trapping",
			"Leatherworking",
			"Woodworking",
			"Metalworking",
			"Tailoring",
			"Mechanics",
			"Apothecary"
		}},
		{ "Life Skills", new string[] {
			"Sincerity",
			"Intimidate",
			"Seduce",
			"Discipline",
			"Persuade",
			"Performance",
			"Streetwise",
			"Survival",
			"Etiquette",
			"Perception",
			"Academics",
			"Leadership",
			"Liturgy"			
		}},
		{ "Perks", new string[] {
			"Alacrity",
			"Ally",
			"Backing",
			"Boon",
			"Fame",
			"Impeccable Memory",
			"Journeyman",
			"Magnetism",
			"Nobody's Fool",
			"Quick Healer",
			"Quiet",
			"Retainer",
			"Slow Bleeder",
			"Spiritual Prodigy",
			"Wealth",
			"Well-Equipped",
			"Workhorse",
			"The Spark",
			"Respected",
			"Hardy",
			"Light Sleeper",
			"Street Savvy",
			"Entrepreneur",
			"Connections", 
			"Classical Education",
			"Highborn",
			"Ice-Hardened",
			"Branded",
			"Tough as Nails", 
			"Collected",
			"Veteran",
			"Loyalty",
			"Humorless",
			"Gnosis",
			"Pious",
			"Natural Linguist",
			"Caravanserai",
			"Magical Wonder",
			"Hard Drinker",
			"Oral Tradition",
			"Ancestral Moorsword",
			"Trade Guild Amici",
			"In Flagrante",
			"Daredevil",
			"Silver Tongue",
			"Elitist",
			"Pistolier"
		}},
		{ "Flaws", new string[] {
			"Beholden",
			"Corpse in the Closet",
			"Dirt Poor",
			"Duty",
			"Enemy",
			"Craven",
			"Cursed",
			"Hedonist",
			"Honor Code",
			"Infamy",
			"Memorable",
			"Naive",
			"Old Wounds",
			"One Eyed Jack",
			"One Foot in the Grave",
			"Pure of Heart",
			"Sick in the Head",
			"Vainglorious",
			"Ward",
			"Wicked",
			"Dainty",
			"Hayseed",
			"Odious",
			"Debt",
			"Entitlement",
			"Thrall of the Old Gods",
			"Pig-Headed",
			"Bigoted",
			"Outspoken Heathen",
			"Harsh Temper",
			"Vendetta",
			"Fop"
		}},
		{ "Traits", new string[] {
			"Abhorrent",
			"Alcoholic",
			"Bravado",
			"Foolish Heart",
			"Death Wish",
			"Finesse Fighter",
			"Heavy Handed", 
			"Renegade"
		}}
	};
	
	string.Format("INSERT INTO attribute_types(id, name) VALUES {0};", string.Join(", ", attributes.Keys.Select((key, id) => string.Format("({0}, \"{1}\")", id + 1, key)))).Dump();
	int currentIndex = 1;
	foreach(var key in attributes.Keys) {
		string.Format("INSERT INTO attributes(attribute_name, attribute_type_id) VALUES {0};",
			string.Join(", ", attributes[key].Select(val => string.Format("(\"{0}\", {1})", val, currentIndex.ToString())))).Dump();
		currentIndex++;
	}
}

// Define other methods and classes here
