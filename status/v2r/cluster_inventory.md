# V2R cluster inventory

2026-09-25T05:59:18.657471+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318868668416 available bytes; 82.21% used; 112480336 free inodes.

server1 `/home`: 318868668416 available bytes; 82.21% used; 112480336 free inodes.

server1 `/tmp`: 318868668416 available bytes; 82.21% used; 112480336 free inodes.

server1 `/var/tmp`: 318868668416 available bytes; 82.21% used; 112480336 free inodes.

server1 `/mnt/raid5`: 408416563200 available bytes; 98.13% used; 337564804 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22903242752 available bytes; 98.72% used; 110410368 free inodes.

server2 `/home`: 22903242752 available bytes; 98.72% used; 110410368 free inodes.

server2 `/tmp`: 22903242752 available bytes; 98.72% used; 110410368 free inodes.

server2 `/var/tmp`: 22903242752 available bytes; 98.72% used; 110410368 free inodes.

server2 `/mnt/raid5`: 393274556416 available bytes; 97.28% used; 445101220 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84314615808 available bytes; 95.29% used; 114156039 free inodes.

server3 `/home`: 84314615808 available bytes; 95.29% used; 114156039 free inodes.

server3 `/data`: 142779523072 available bytes; 98.03% used; 225814325 free inodes.

server3 `/tmp`: 84314615808 available bytes; 95.29% used; 114156039 free inodes.

server3 `/var/tmp`: 84314615808 available bytes; 95.29% used; 114156039 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105649135616 available bytes; 94.10% used; 114350386 free inodes.

server4 `/home`: 105649135616 available bytes; 94.10% used; 114350386 free inodes.

server4 `/data`: 256294592512 available bytes; 96.46% used; 225025883 free inodes.

server4 `/tmp`: 105649135616 available bytes; 94.10% used; 114350386 free inodes.

server4 `/var/tmp`: 105649135616 available bytes; 94.10% used; 114350386 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
