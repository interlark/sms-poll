import {
    IconButton,
    Text,
    VStack,
    Link,
    HStack,
} from "@chakra-ui/react"
import { TbExternalLink } from "react-icons/tb"
import { HiWifi } from "react-icons/hi"


function PollInfo({wifiIP, updateWifiIP}) {
    const isValdIP = ip => {
        const pattern = /^(?!0)(?!.*\.$)((1?\d?\d|25[0-5]|2[0-4]\d)(\.|$)){4}$/
        return pattern.test(ip)
    }
    const pollURL = `http://${wifiIP}:${location.port}/poll`
    const textStyle = () => {
        return ({
            sx: { "&&": { marginInlineStart: "0.8rem" },
        }})
    }

    return (
        <VStack mt="4">
            <VStack alignItems="start">
                <HStack>
                    <IconButton
                        icon={<HiWifi />}
                        isRound="true"
                        size="md"
                        onClick={updateWifiIP}
                    />
                    <Text {...textStyle()}>{wifiIP}</Text>
                </HStack>

                <HStack>
                    <IconButton
                        icon={<TbExternalLink />}
                        isRound="true"
                        size="md"
                        onClick={updateWifiIP}
                    />
                    { isValdIP(wifiIP) ?
                        <Link
                            href={pollURL}
                            textDecor="underline" isExternal
                            {...textStyle()}
                        >
                        {pollURL}
                        </Link>
                        :
                        <Text {...textStyle()}>Not available</Text>
                    }
                </HStack>
            </VStack>
        </VStack>
    )
}

export default PollInfo