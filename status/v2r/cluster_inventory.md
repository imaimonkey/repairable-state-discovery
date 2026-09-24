# V2R cluster inventory

2026-09-24T19:44:48.380291+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 323989147648 available bytes; 81.93% used; 112481463 free inodes.

server1 `/home`: 323989147648 available bytes; 81.93% used; 112481463 free inodes.

server1 `/tmp`: 323989147648 available bytes; 81.93% used; 112481463 free inodes.

server1 `/var/tmp`: 323989147648 available bytes; 81.93% used; 112481463 free inodes.

server1 `/mnt/raid5`: 415588478976 available bytes; 98.09% used; 337630654 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 44744015872 available bytes; 97.50% used; 110411693 free inodes.

server2 `/home`: 44744015872 available bytes; 97.50% used; 110411693 free inodes.

server2 `/tmp`: 44744015872 available bytes; 97.50% used; 110411693 free inodes.

server2 `/var/tmp`: 44744015872 available bytes; 97.50% used; 110411693 free inodes.

server2 `/mnt/raid5`: 494410174464 available bytes; 96.58% used; 445158276 free inodes.
| server3 | True | ['1'] | [] | reference_compatible=True |

server3 `/`: 84400177152 available bytes; 95.29% used; 114156139 free inodes.

server3 `/home`: 84400177152 available bytes; 95.29% used; 114156139 free inodes.

server3 `/data`: 152131956736 available bytes; 97.90% used; 225799229 free inodes.

server3 `/tmp`: 84400177152 available bytes; 95.29% used; 114156139 free inodes.

server3 `/var/tmp`: 84400177152 available bytes; 95.29% used; 114156139 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105642311680 available bytes; 94.10% used; 114348430 free inodes.

server4 `/home`: 105642311680 available bytes; 94.10% used; 114348430 free inodes.

server4 `/data`: 89851944960 available bytes; 98.76% used; 225266561 free inodes.

server4 `/tmp`: 105642311680 available bytes; 94.10% used; 114348430 free inodes.

server4 `/var/tmp`: 105642311680 available bytes; 94.10% used; 114348430 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
