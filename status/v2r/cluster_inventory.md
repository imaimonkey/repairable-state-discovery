# V2R cluster inventory

2026-09-26T10:58:37.346123+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318214488064 available bytes; 82.25% used; 112474830 free inodes.

server1 `/home`: 318214488064 available bytes; 82.25% used; 112474830 free inodes.

server1 `/tmp`: 318214488064 available bytes; 82.25% used; 112474830 free inodes.

server1 `/var/tmp`: 318214488064 available bytes; 82.25% used; 112474830 free inodes.

server1 `/mnt/raid5`: 218766204928 available bytes; 99.00% used; 337538225 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 19853012992 available bytes; 98.89% used; 110384899 free inodes.

server2 `/home`: 19853012992 available bytes; 98.89% used; 110384899 free inodes.

server2 `/tmp`: 19853012992 available bytes; 98.89% used; 110384899 free inodes.

server2 `/var/tmp`: 19853012992 available bytes; 98.89% used; 110384899 free inodes.

server2 `/mnt/raid5`: 242390384640 available bytes; 98.33% used; 444979294 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82662858752 available bytes; 95.39% used; 114110819 free inodes.

server3 `/home`: 82662858752 available bytes; 95.39% used; 114110819 free inodes.

server3 `/data`: 123568738304 available bytes; 98.29% used; 225826050 free inodes.

server3 `/tmp`: 82662858752 available bytes; 95.39% used; 114110819 free inodes.

server3 `/var/tmp`: 82662858752 available bytes; 95.39% used; 114110819 free inodes.
| server4 | True | ['3', '4', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105926684672 available bytes; 94.09% used; 114347962 free inodes.

server4 `/home`: 105926684672 available bytes; 94.09% used; 114347962 free inodes.

server4 `/data`: 88893898752 available bytes; 98.77% used; 224880563 free inodes.

server4 `/tmp`: 105926684672 available bytes; 94.09% used; 114347962 free inodes.

server4 `/var/tmp`: 105926684672 available bytes; 94.09% used; 114347962 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
