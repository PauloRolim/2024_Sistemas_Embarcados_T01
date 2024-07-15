/* WARNING : LCHIP system source file, do not edit */

MACHINE
    user_component
SEES
    g_types
OPERATIONS
    user_app = skip;

    user_consistency_error_detection_test(divergence_value) =
    PRE
        divergence_value : uint8_t
    THEN
        skip
    END
END
