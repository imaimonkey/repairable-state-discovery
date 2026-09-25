# V2R cluster inventory

2026-09-25T11:27:21.523054+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319063638016 available bytes; 82.20% used; 112478824 free inodes.

server1 `/home`: 319063638016 available bytes; 82.20% used; 112478824 free inodes.

server1 `/tmp`: 319063638016 available bytes; 82.20% used; 112478824 free inodes.

server1 `/var/tmp`: 319063638016 available bytes; 82.20% used; 112478824 free inodes.

server1 `/mnt/raid5`: 364210307072 available bytes; 98.33% used; 337550272 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 22911098880 available bytes; 98.72% used; 110409978 free inodes.

server2 `/home`: 22911098880 available bytes; 98.72% used; 110409978 free inodes.

server2 `/tmp`: 22911098880 available bytes; 98.72% used; 110409978 free inodes.

server2 `/var/tmp`: 22911098880 available bytes; 98.72% used; 110409978 free inodes.

server2 `/mnt/raid5`: 327737049088 available bytes; 97.74% used; 445083697 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84135178240 available bytes; 95.30% used; 114155498 free inodes.

server3 `/home`: 84135178240 available bytes; 95.30% used; 114155498 free inodes.

server3 `/data`: 142081236992 available bytes; 98.04% used; 225814213 free inodes.

server3 `/tmp`: 84135178240 available bytes; 95.30% used; 114155498 free inodes.

server3 `/var/tmp`: 84135178240 available bytes; 95.30% used; 114155498 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105603276800 available bytes; 94.11% used; 114350250 free inodes.

server4 `/home`: 105603276800 available bytes; 94.11% used; 114350250 free inodes.

server4 `/data`: 238165962752 available bytes; 96.71% used; 224978816 free inodes.

server4 `/tmp`: 105603276800 available bytes; 94.11% used; 114350250 free inodes.

server4 `/var/tmp`: 105603276800 available bytes; 94.11% used; 114350250 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
