from Bio import PDB

def extract_ligand(input_pdb, ligand_id, output_pdb):
    parser = PDB.PDBParser(QUIET=True)
    structure = parser.get_structure('structure', input_pdb)

    io = PDB.PDBIO()
    io.set_structure(structure)

    for model in structure:
        for chain in model:
            for residue in chain:
                if residue.id == ligand_id:
                    io.save(output_pdb, select=ligand_id)
                    print(f"Ligand '{ligand_id}' extracted and saved to '{output_pdb}'")
                    return

if __name__ == "__main__":
    input_pdb_file = "your_structure.pdb"
    ligand_identifier = (" ", 1, " ")  # Replace with the actual identifier of your ligand
    output_pdb_file = "extracted_ligand.pdb"

    extract_ligand(input_pdb_file, ligand_identifier, output_pdb_file)
