# V2R cluster inventory

2026-09-25T11:30:24.996409+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319064125440 available bytes; 82.20% used; 112478822 free inodes.

server1 `/home`: 319064125440 available bytes; 82.20% used; 112478822 free inodes.

server1 `/tmp`: 319064125440 available bytes; 82.20% used; 112478822 free inodes.

server1 `/var/tmp`: 319064125440 available bytes; 82.20% used; 112478822 free inodes.

server1 `/mnt/raid5`: 364208701440 available bytes; 98.33% used; 337550261 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 22911643648 available bytes; 98.72% used; 110409980 free inodes.

server2 `/home`: 22911643648 available bytes; 98.72% used; 110409980 free inodes.

server2 `/tmp`: 22911643648 available bytes; 98.72% used; 110409980 free inodes.

server2 `/var/tmp`: 22911643648 available bytes; 98.72% used; 110409980 free inodes.

server2 `/mnt/raid5`: 327627624448 available bytes; 97.74% used; 445083489 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84133187584 available bytes; 95.31% used; 114155500 free inodes.

server3 `/home`: 84133187584 available bytes; 95.31% used; 114155500 free inodes.

server3 `/data`: 142080720896 available bytes; 98.04% used; 225814178 free inodes.

server3 `/tmp`: 84133187584 available bytes; 95.31% used; 114155500 free inodes.

server3 `/var/tmp`: 84133187584 available bytes; 95.31% used; 114155500 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105603162112 available bytes; 94.11% used; 114350248 free inodes.

server4 `/home`: 105603162112 available bytes; 94.11% used; 114350248 free inodes.

server4 `/data`: 237368414208 available bytes; 96.72% used; 224978395 free inodes.

server4 `/tmp`: 105603162112 available bytes; 94.11% used; 114350248 free inodes.

server4 `/var/tmp`: 105603162112 available bytes; 94.11% used; 114350248 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
