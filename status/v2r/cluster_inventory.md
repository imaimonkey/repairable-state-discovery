# V2R cluster inventory

2026-09-27T02:43:10.386125+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315079028736 available bytes; 82.42% used; 112443409 free inodes.

server1 `/home`: 315079028736 available bytes; 82.42% used; 112443409 free inodes.

server1 `/tmp`: 315079028736 available bytes; 82.42% used; 112443409 free inodes.

server1 `/var/tmp`: 315079028736 available bytes; 82.42% used; 112443409 free inodes.

server1 `/mnt/raid5`: 637203070976 available bytes; 97.08% used; 337401566 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17625743360 available bytes; 99.02% used; 110365006 free inodes.

server2 `/home`: 17625743360 available bytes; 99.02% used; 110365006 free inodes.

server2 `/tmp`: 17625743360 available bytes; 99.02% used; 110365006 free inodes.

server2 `/var/tmp`: 17625743360 available bytes; 99.02% used; 110365006 free inodes.

server2 `/mnt/raid5`: 580590747648 available bytes; 95.99% used; 444884114 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78706733056 available bytes; 95.61% used; 114062953 free inodes.

server3 `/home`: 78706733056 available bytes; 95.61% used; 114062953 free inodes.

server3 `/data`: 1336617218048 available bytes; 81.53% used; 225762163 free inodes.

server3 `/tmp`: 78706733056 available bytes; 95.61% used; 114062953 free inodes.

server3 `/var/tmp`: 78706733056 available bytes; 95.61% used; 114062953 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111036002304 available bytes; 93.80% used; 114373249 free inodes.

server4 `/home`: 111036002304 available bytes; 93.80% used; 114373249 free inodes.

server4 `/data`: 397015564288 available bytes; 94.51% used; 224781463 free inodes.

server4 `/tmp`: 111036002304 available bytes; 93.80% used; 114373249 free inodes.

server4 `/var/tmp`: 111036002304 available bytes; 93.80% used; 114373249 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
