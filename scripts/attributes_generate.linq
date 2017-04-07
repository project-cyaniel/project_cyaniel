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
		}},
		{ "Cultures", new string[] {
			"Capacionne",
			"Dunnick",
			"Gothic",
			"Hestrali",
			"Njordic",
			"Rogalian",
			"Shariqyn"
		}},
		{ "Social Classes", new string[] {
			"Scum",
			"Peasant",
			"Merchant",
			"Gentry"
		}}
	};
	
	var socialClassSkills = new Dictionary<string, string[]> {
		{ "Scum", new string[] {
			"Streetwise",
			"Sincerity",
			"Intimidate",
			"Finesse",
			"Stealth"
		}},
		{ "Peasant", new string[] {
			"Perception",
			"Liturgy",
			"Grit",
			"Survival",
			"Farming",
			"Forestry",
			"Herbalism",
			"Trapping",
			"Mining"
		}},
		{ "Merchant", new string[] {
			"Mercantile",
			"Perception",
			"Survival",
			"Sincerity",
			"Leatherworking",
			"Woodworking",
			"Metalworking",
			"Tailoring",
			"Mechanics"
		}},
		{ "Gentry", new string[] {
			"Medium Weapons",
			"Etiquette",
			"Academics",
			"Intimidate",
			"Leadership"
		}}
	};
	
	var cultureSkills = new Dictionary<string, string[]> {
		{ "Capacionne", new string[] {
			"Firearms",
			"Trapping",
			"Mechanics",
			"Seduce",
			"Persuade"
		}},
		{ "Dunnick", new string[] {
			"Brawl",
			"Grit",
			"Herbalism",
			"Mining",
			"Apothecary"
		}},
		{ "Gothic", new string[] {
			"Discipline",
			"Farming",
			"Medium Weapons",
			"Leadership",
			"Liturgy"
		}},
		{ "Hestrali", new string[] {
			"Mercantile",
			"Mobility",
			"Seduce",
			"Finesse",
			"Performance"
		}},
		{ "Njordic", new string[] {
			"Survival",
			"Grit",
			"Intimidate",
			"Performance",
			"Forestry"
		}},
		{ "Rogalian", new string[] {
			"Archery",
			"Etiquette",
			"Metalworking",
			"Discipline",
			"Perception"
		}},
		{ "Shariqyn", new string[] {
			"Academics",
			"Mercantile",
			"Survival",
			"Persuade",
			"Liturgy"
		}}
	};
	
	string.Format("INSERT INTO attribute_types(id, name) VALUES {0};", string.Join(", ", attributes.Keys.Select((key, id) => string.Format("({0}, \"{1}\")", id + 1, key)))).Dump();
	int currentIndex = 1;
	foreach(var key in attributes.Keys) {
		string.Format("INSERT INTO attributes(attribute_name, attribute_type_id) VALUES {0};",
			string.Join(", ", attributes[key].Select(val => string.Format("(\"{0}\", {1})", val, currentIndex.ToString())))).Dump();
		currentIndex++;
	}
	
	Console.Write("Paste what's currently in the console to the DB, press enter when ready to continue...");
	Console.Read();
	"".Dump();
	"INSERT INTO advancement_lists(name,is_chargen_only) VALUES('Social Status', 1), ('Culture', 1), ('Social Status Skills', 1), ('Culture Skills', 1);".Dump();
	"".Dump();
		
	int last_list_attribute_id = 1;
	foreach(var social in socialClassSkills.Keys) {
		var social_row = Attributes.FirstOrDefault (s => s.Attribute_name == social);
		if(social_row == null) {
			throw new Exception("Unable to find social status: " + social);
		}
		
		string.Format("INSERT INTO advancement_list_attributes (id, advancement_list_id, attribute_id) VALUES({0}, {1}, {2});", last_list_attribute_id,
			1, social_row.Id).Dump();
		last_list_attribute_id++;
	}
	
	foreach(var culture in cultureSkills.Keys) {
		var culture_row = Attributes.FirstOrDefault(a => a.Attribute_name == culture);
		if(culture_row == null) {
			throw new Exception("Unable to find culture: " + culture);
		}
		string.Format("INSERT INTO advancement_list_attributes (id, advancement_list_id, attribute_id) VALUES({0}, {1}, {2});", last_list_attribute_id,
			2, culture_row.Id).Dump();
		last_list_attribute_id++;
	}
	
	foreach(var culture in cultureSkills.Keys) {
		var culture_row = Attributes.FirstOrDefault(a => a.Attribute_name == culture);
		if(culture_row == null) {
			throw new Exception("Unable to find culture: " + culture);
		}
		foreach(var skill in cultureSkills[culture]) {
			var skill_id = Attributes.FirstOrDefault (s => s.Attribute_name == skill);
			if(skill_id == null) {
				throw new Exception("Unable to find skill: " + skill);
			}
			string.Format("INSERT INTO advancement_list_attributes (id, advancement_list_id, attribute_id) VALUES({0}, 4, {1});", last_list_attribute_id, skill_id.Id).Dump();
			string.Format("INSERT INTO advancement_list_requirements(advancement_list_attribute_id, attribute_requirement_id) VALUES({0}, {1});", last_list_attribute_id, culture_row.Id).Dump();
			
			last_list_attribute_id++;			
		}
	}
		
	foreach(var social in socialClassSkills.Keys) {
		var social_row = Attributes.FirstOrDefault (s => s.Attribute_name == social);
		if(social_row == null) {
			throw new Exception("Unable to find social status: " + social);
		}
		
		foreach(var skill in socialClassSkills[social]) {
			var skill_id = Attributes.FirstOrDefault (s => s.Attribute_name == skill);
			if(skill_id == null) {
				throw new Exception("Unable to find skill: " + skill);
			}
			
			string.Format("INSERT INTO advancement_list_attributes (id, advancement_list_id, attribute_id) VALUES({0}, 4, {1});", last_list_attribute_id, skill_id.Id).Dump();
			string.Format("INSERT INTO advancement_list_requirements(advancement_list_attribute_id, attribute_requirement_id) VALUES({0}, {1});", last_list_attribute_id, social_row.Id).Dump();
			
			last_list_attribute_id++;
		}
	}
}

// Define other methods and classes here
