# V2R cluster inventory

2026-09-25T20:22:42.541686+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318706769920 available bytes; 82.22% used; 112476331 free inodes.

server1 `/home`: 318706769920 available bytes; 82.22% used; 112476331 free inodes.

server1 `/tmp`: 318706769920 available bytes; 82.22% used; 112476331 free inodes.

server1 `/var/tmp`: 318706769920 available bytes; 82.22% used; 112476331 free inodes.

server1 `/mnt/raid5`: 369633681408 available bytes; 98.30% used; 337540528 free inodes.
| server2 | True | ['4', '5', '6'] | [] |

server2 `/`: 23061225472 available bytes; 98.71% used; 110407439 free inodes.

server2 `/home`: 23061188608 available bytes; 98.71% used; 110407439 free inodes.

server2 `/tmp`: 23061164032 available bytes; 98.71% used; 110407439 free inodes.

server2 `/var/tmp`: 23061147648 available bytes; 98.71% used; 110407439 free inodes.

server2 `/mnt/raid5`: 303532544000 available bytes; 97.90% used; 445058493 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84379545600 available bytes; 95.29% used; 114152620 free inodes.

server3 `/home`: 84379545600 available bytes; 95.29% used; 114152620 free inodes.

server3 `/data`: 127185903616 available bytes; 98.24% used; 225808171 free inodes.

server3 `/tmp`: 84379545600 available bytes; 95.29% used; 114152620 free inodes.

server3 `/var/tmp`: 84379545600 available bytes; 95.29% used; 114152620 free inodes.
| server4 | True | ['3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105664737280 available bytes; 94.10% used; 114349569 free inodes.

server4 `/home`: 105664737280 available bytes; 94.10% used; 114349569 free inodes.

server4 `/data`: 228739420160 available bytes; 96.84% used; 224928871 free inodes.

server4 `/tmp`: 105664737280 available bytes; 94.10% used; 114349569 free inodes.

server4 `/var/tmp`: 105664737280 available bytes; 94.10% used; 114349569 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
