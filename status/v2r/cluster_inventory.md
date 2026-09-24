# V2R cluster inventory

2026-09-24T04:01:00.255538+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324723376128 available bytes; 81.88% used; 112493537 free inodes.

server1 `/home`: 324723376128 available bytes; 81.88% used; 112493537 free inodes.

server1 `/tmp`: 324723376128 available bytes; 81.88% used; 112493537 free inodes.

server1 `/var/tmp`: 324723376128 available bytes; 81.88% used; 112493537 free inodes.

server1 `/mnt/raid5`: 416634621952 available bytes; 98.09% used; 337724773 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40811474944 available bytes; 97.72% used; 110430868 free inodes.

server2 `/home`: 40811474944 available bytes; 97.72% used; 110430868 free inodes.

server2 `/tmp`: 40811474944 available bytes; 97.72% used; 110430868 free inodes.

server2 `/var/tmp`: 40811474944 available bytes; 97.72% used; 110430868 free inodes.

server2 `/mnt/raid5`: 526253633536 available bytes; 96.36% used; 445196877 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 291986100224 available bytes; 83.71% used; 114177495 free inodes.

server3 `/home`: 291986100224 available bytes; 83.71% used; 114177495 free inodes.

server3 `/data`: 33868120064 available bytes; 99.53% used; 225842389 free inodes.

server3 `/tmp`: 291986100224 available bytes; 83.71% used; 114177495 free inodes.

server3 `/var/tmp`: 291986100224 available bytes; 83.71% used; 114177495 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105791369216 available bytes; 94.10% used; 114349504 free inodes.

server4 `/home`: 105791369216 available bytes; 94.10% used; 114349504 free inodes.

server4 `/data`: 258349260800 available bytes; 96.43% used; 225382392 free inodes.

server4 `/tmp`: 105791369216 available bytes; 94.10% used; 114349504 free inodes.

server4 `/var/tmp`: 105791369216 available bytes; 94.10% used; 114349504 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
