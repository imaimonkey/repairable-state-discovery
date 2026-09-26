# V2R cluster inventory

2026-09-26T01:32:18.390284+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318648799232 available bytes; 82.22% used; 112476297 free inodes.

server1 `/home`: 318648799232 available bytes; 82.22% used; 112476297 free inodes.

server1 `/tmp`: 318648799232 available bytes; 82.22% used; 112476297 free inodes.

server1 `/var/tmp`: 318648799232 available bytes; 82.22% used; 112476297 free inodes.

server1 `/mnt/raid5`: 345494413312 available bytes; 98.42% used; 337546537 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22929096704 available bytes; 98.72% used; 110406216 free inodes.

server2 `/home`: 22929096704 available bytes; 98.72% used; 110406216 free inodes.

server2 `/tmp`: 22929096704 available bytes; 98.72% used; 110406216 free inodes.

server2 `/var/tmp`: 22929096704 available bytes; 98.72% used; 110406216 free inodes.

server2 `/mnt/raid5`: 290637881344 available bytes; 97.99% used; 445055727 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84335796224 available bytes; 95.29% used; 114152426 free inodes.

server3 `/home`: 84335796224 available bytes; 95.29% used; 114152426 free inodes.

server3 `/data`: 124869332992 available bytes; 98.27% used; 225817978 free inodes.

server3 `/tmp`: 84335796224 available bytes; 95.29% used; 114152426 free inodes.

server3 `/var/tmp`: 84335796224 available bytes; 95.29% used; 114152426 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105196916736 available bytes; 94.13% used; 114346905 free inodes.

server4 `/home`: 105196916736 available bytes; 94.13% used; 114346905 free inodes.

server4 `/data`: 134785196032 available bytes; 98.14% used; 224917281 free inodes.

server4 `/tmp`: 105196916736 available bytes; 94.13% used; 114346905 free inodes.

server4 `/var/tmp`: 105196916736 available bytes; 94.13% used; 114346905 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
