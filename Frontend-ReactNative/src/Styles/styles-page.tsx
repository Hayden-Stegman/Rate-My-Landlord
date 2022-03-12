import { StyleSheet } from "react-native";
import { ThemeColors } from "../constants/Colors";

export default StyleSheet.create({
    // Back Ground Container - Holds all
    backgroundScreen: {
        flex: 1,
    },
    // Right Ad Container for potential Ad Space - (Web Only)
    rightContainer: {
        flex: 1,
        marginHorizontal: 10,
        marginBottom: 10,
        borderRadius: 15,

        // Temp?
        backgroundColor: ThemeColors.white,
        justifyContent: 'center',
        alignItems: 'center',
    },
    // General Text color for Paragraphs and such
    textColor: {
        color: ThemeColors.darkBlue,
    },
    flatList: {
        width: '100%',
        height: '100%',
        padding: 15,
    },
})