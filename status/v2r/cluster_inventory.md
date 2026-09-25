# V2R cluster inventory

2026-09-25T15:15:17.911828+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319043579904 available bytes; 82.20% used; 112476385 free inodes.

server1 `/home`: 319043579904 available bytes; 82.20% used; 112476385 free inodes.

server1 `/tmp`: 319043579904 available bytes; 82.20% used; 112476385 free inodes.

server1 `/var/tmp`: 319043579904 available bytes; 82.20% used; 112476385 free inodes.

server1 `/mnt/raid5`: 363963494400 available bytes; 98.33% used; 337545923 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 23109312512 available bytes; 98.71% used; 110407927 free inodes.

server2 `/home`: 23109312512 available bytes; 98.71% used; 110407927 free inodes.

server2 `/tmp`: 23109312512 available bytes; 98.71% used; 110407927 free inodes.

server2 `/var/tmp`: 23109312512 available bytes; 98.71% used; 110407927 free inodes.

server2 `/mnt/raid5`: 320389292032 available bytes; 97.79% used; 445073448 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84425695232 available bytes; 95.29% used; 114153448 free inodes.

server3 `/home`: 84425695232 available bytes; 95.29% used; 114153448 free inodes.

server3 `/data`: 142179942400 available bytes; 98.04% used; 225807970 free inodes.

server3 `/tmp`: 84425695232 available bytes; 95.29% used; 114153448 free inodes.

server3 `/var/tmp`: 84425695232 available bytes; 95.29% used; 114153448 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105638346752 available bytes; 94.10% used; 114349692 free inodes.

server4 `/home`: 105638346752 available bytes; 94.10% used; 114349692 free inodes.

server4 `/data`: 231347556352 available bytes; 96.80% used; 224944736 free inodes.

server4 `/tmp`: 105638346752 available bytes; 94.10% used; 114349692 free inodes.

server4 `/var/tmp`: 105638346752 available bytes; 94.10% used; 114349692 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
