# V2R cluster inventory

2026-09-23T20:24:35.337044+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325736460288 available bytes; 81.83% used; 112501777 free inodes.

server1 `/home`: 325736460288 available bytes; 81.83% used; 112501777 free inodes.

server1 `/tmp`: 325736460288 available bytes; 81.83% used; 112501777 free inodes.

server1 `/var/tmp`: 325736460288 available bytes; 81.83% used; 112501777 free inodes.

server1 `/mnt/raid5`: 1388280209408 available bytes; 93.63% used; 337740990 free inodes.
| server2 | True | ['2', '3', '4', '5'] | [] |

server2 `/`: 41142382592 available bytes; 97.70% used; 110432828 free inodes.

server2 `/home`: 41142382592 available bytes; 97.70% used; 110432828 free inodes.

server2 `/tmp`: 41142382592 available bytes; 97.70% used; 110432828 free inodes.

server2 `/var/tmp`: 41142382592 available bytes; 97.70% used; 110432828 free inodes.

server2 `/mnt/raid5`: 541092335616 available bytes; 96.26% used; 445210665 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 293332582400 available bytes; 83.63% used; 114232752 free inodes.

server3 `/home`: 293332574208 available bytes; 83.63% used; 114232751 free inodes.

server3 `/data`: 52607242240 available bytes; 99.27% used; 225843805 free inodes.

server3 `/tmp`: 293332566016 available bytes; 83.63% used; 114232751 free inodes.

server3 `/var/tmp`: 293332566016 available bytes; 83.63% used; 114232751 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106527784960 available bytes; 94.06% used; 114356185 free inodes.

server4 `/home`: 106527784960 available bytes; 94.06% used; 114356185 free inodes.

server4 `/data`: 8007680 available bytes; 100.00% used; 225457623 free inodes.

server4 `/tmp`: 106527784960 available bytes; 94.06% used; 114356185 free inodes.

server4 `/var/tmp`: 106527784960 available bytes; 94.06% used; 114356185 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
