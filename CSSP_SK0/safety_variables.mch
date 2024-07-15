/* WARNING : LCHIP system source file, do not edit */

MACHINE
    safety_variables
SEES
    g_types
CONCRETE_VARIABLES
    safety_variables_array
INVARIANT
    safety_variables_array : 0..struct_safety_variables_size_minus_1 --> uint8_t
INITIALISATION
    safety_variables_array :: 0..struct_safety_variables_size_minus_1 --> uint8_t
CONCRETE_CONSTANTS
    struct_safety_variables_size_minus_1
PROPERTIES
    struct_safety_variables_size_minus_1 : uint32_t &
    struct_safety_variables_size_minus_1 < MAX_UINT32
END
