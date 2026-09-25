# V2R cluster inventory

2026-09-25T08:28:20.530070+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318826127360 available bytes; 82.21% used; 112480360 free inodes.

server1 `/home`: 318826127360 available bytes; 82.21% used; 112480360 free inodes.

server1 `/tmp`: 318826127360 available bytes; 82.21% used; 112480360 free inodes.

server1 `/var/tmp`: 318826127360 available bytes; 82.21% used; 112480360 free inodes.

server1 `/mnt/raid5`: 364232392704 available bytes; 98.33% used; 337557099 free inodes.
| server2 | True | ['5', '6'] | [] | reference_compatible=False |

server2 `/`: 22832693248 available bytes; 98.73% used; 110410490 free inodes.

server2 `/home`: 22832693248 available bytes; 98.73% used; 110410490 free inodes.

server2 `/tmp`: 22832693248 available bytes; 98.73% used; 110410490 free inodes.

server2 `/var/tmp`: 22832693248 available bytes; 98.73% used; 110410490 free inodes.

server2 `/mnt/raid5`: 333345689600 available bytes; 97.70% used; 445094337 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84438872064 available bytes; 95.29% used; 114156052 free inodes.

server3 `/home`: 84438872064 available bytes; 95.29% used; 114156052 free inodes.

server3 `/data`: 142381682688 available bytes; 98.03% used; 225811696 free inodes.

server3 `/tmp`: 84438872064 available bytes; 95.29% used; 114156052 free inodes.

server3 `/var/tmp`: 84438872064 available bytes; 95.29% used; 114156052 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105685610496 available bytes; 94.10% used; 114350334 free inodes.

server4 `/home`: 105685610496 available bytes; 94.10% used; 114350334 free inodes.

server4 `/data`: 246760800256 available bytes; 96.59% used; 225005146 free inodes.

server4 `/tmp`: 105685610496 available bytes; 94.10% used; 114350334 free inodes.

server4 `/var/tmp`: 105685610496 available bytes; 94.10% used; 114350334 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
