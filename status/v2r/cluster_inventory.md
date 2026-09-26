# V2R cluster inventory

2026-09-26T03:00:51.073383+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318417313792 available bytes; 82.24% used; 112476267 free inodes.

server1 `/home`: 318417313792 available bytes; 82.24% used; 112476267 free inodes.

server1 `/tmp`: 318417313792 available bytes; 82.24% used; 112476267 free inodes.

server1 `/var/tmp`: 318417313792 available bytes; 82.24% used; 112476267 free inodes.

server1 `/mnt/raid5`: 331084292096 available bytes; 98.48% used; 337545962 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22942273536 available bytes; 98.72% used; 110406216 free inodes.

server2 `/home`: 22942273536 available bytes; 98.72% used; 110406216 free inodes.

server2 `/tmp`: 22942273536 available bytes; 98.72% used; 110406216 free inodes.

server2 `/var/tmp`: 22942273536 available bytes; 98.72% used; 110406216 free inodes.

server2 `/mnt/raid5`: 288069459968 available bytes; 98.01% used; 445053350 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84309254144 available bytes; 95.30% used; 114152372 free inodes.

server3 `/home`: 84309254144 available bytes; 95.30% used; 114152372 free inodes.

server3 `/data`: 125441994752 available bytes; 98.27% used; 225831181 free inodes.

server3 `/tmp`: 84309254144 available bytes; 95.30% used; 114152372 free inodes.

server3 `/var/tmp`: 84309254144 available bytes; 95.30% used; 114152372 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105918828544 available bytes; 94.09% used; 114347151 free inodes.

server4 `/home`: 105918828544 available bytes; 94.09% used; 114347151 free inodes.

server4 `/data`: 109711724544 available bytes; 98.48% used; 224915370 free inodes.

server4 `/tmp`: 105918828544 available bytes; 94.09% used; 114347151 free inodes.

server4 `/var/tmp`: 105918828544 available bytes; 94.09% used; 114347151 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
