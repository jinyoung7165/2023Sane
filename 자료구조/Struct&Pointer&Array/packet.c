#include <stdio.h>
#include <stdint.h>

// Struct Packet_s 선언
typedef struct packet_s
{
	uint8_t data0;
	uint8_t data1;
	uint8_t data2;
	uint8_t data3;

} Packet_s;

typedef union packet_u
{
	Packet_s ps;  // Struct Packet_s ps 정의 // 송신
	uint8_t pu[4];  // 수신
} Packet_u;


int main()
{
	Packet_u packet_data;

	packet_data.ps.data0 = 0;  // 예를 들어 uuid
	packet_data.ps.data1 = 1;  // minor
	packet_data.ps.data2 = 2;  // tx power
	packet_data.ps.data3 = 3;  // rssi

	// 4 bytes
	printf("pacekt_data size = %d bytes\n\n", sizeof(packet_data));

	// 4 bytes
	printf("송신 사이즈 : %d bytes\n\n", sizeof(packet_data.ps));

	printf("--------------------------\n");
	printf("-------송수신 완료--------\n\n");

	// 4 bytes
	printf("수신 사이즈 : %d bytes\n", sizeof(packet_data.pu));
	printf("uuid = %d\n", packet_data.pu[0]); //0
	printf("minor = %d\n", packet_data.pu[1]); //1
	printf("tx power = %d\n", packet_data.pu[2]); //2
	printf("rssi = %d\n", packet_data.pu[3]); //3

	return 0;
}