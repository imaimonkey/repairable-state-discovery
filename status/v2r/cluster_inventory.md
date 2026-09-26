# V2R cluster inventory

2026-09-26T00:37:23.072888+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318651518976 available bytes; 82.22% used; 112476299 free inodes.

server1 `/home`: 318651518976 available bytes; 82.22% used; 112476299 free inodes.

server1 `/tmp`: 318651518976 available bytes; 82.22% used; 112476299 free inodes.

server1 `/var/tmp`: 318651518976 available bytes; 82.22% used; 112476299 free inodes.

server1 `/mnt/raid5`: 345621233664 available bytes; 98.41% used; 337546810 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22942294016 available bytes; 98.72% used; 110406214 free inodes.

server2 `/home`: 22942294016 available bytes; 98.72% used; 110406214 free inodes.

server2 `/tmp`: 22942294016 available bytes; 98.72% used; 110406214 free inodes.

server2 `/var/tmp`: 22942294016 available bytes; 98.72% used; 110406214 free inodes.

server2 `/mnt/raid5`: 294878142464 available bytes; 97.96% used; 445057684 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84341891072 available bytes; 95.29% used; 114152439 free inodes.

server3 `/home`: 84341891072 available bytes; 95.29% used; 114152439 free inodes.

server3 `/data`: 124943085568 available bytes; 98.27% used; 225818922 free inodes.

server3 `/tmp`: 84341891072 available bytes; 95.29% used; 114152439 free inodes.

server3 `/var/tmp`: 84341891072 available bytes; 95.29% used; 114152439 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105349578752 available bytes; 94.12% used; 114347253 free inodes.

server4 `/home`: 105349578752 available bytes; 94.12% used; 114347253 free inodes.

server4 `/data`: 148732932096 available bytes; 97.94% used; 224917402 free inodes.

server4 `/tmp`: 105349578752 available bytes; 94.12% used; 114347253 free inodes.

server4 `/var/tmp`: 105349578752 available bytes; 94.12% used; 114347253 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
