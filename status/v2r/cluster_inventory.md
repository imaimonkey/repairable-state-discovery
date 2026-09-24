# V2R cluster inventory

2026-09-24T19:41:42.390162+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 323989684224 available bytes; 81.93% used; 112481457 free inodes.

server1 `/home`: 323989684224 available bytes; 81.93% used; 112481457 free inodes.

server1 `/tmp`: 323989684224 available bytes; 81.93% used; 112481457 free inodes.

server1 `/var/tmp`: 323989684224 available bytes; 81.93% used; 112481457 free inodes.

server1 `/mnt/raid5`: 415595253760 available bytes; 98.09% used; 337631015 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 48390524928 available bytes; 97.30% used; 110411742 free inodes.

server2 `/home`: 48390524928 available bytes; 97.30% used; 110411742 free inodes.

server2 `/tmp`: 48390524928 available bytes; 97.30% used; 110411742 free inodes.

server2 `/var/tmp`: 48390524928 available bytes; 97.30% used; 110411742 free inodes.

server2 `/mnt/raid5`: 493979308032 available bytes; 96.59% used; 445158586 free inodes.
| server3 | True | ['1'] | [] | reference_compatible=True |

server3 `/`: 84400640000 available bytes; 95.29% used; 114156139 free inodes.

server3 `/home`: 84400640000 available bytes; 95.29% used; 114156139 free inodes.

server3 `/data`: 152167141376 available bytes; 97.90% used; 225799286 free inodes.

server3 `/tmp`: 84400640000 available bytes; 95.29% used; 114156139 free inodes.

server3 `/var/tmp`: 84400640000 available bytes; 95.29% used; 114156139 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105650802688 available bytes; 94.10% used; 114348431 free inodes.

server4 `/home`: 105650802688 available bytes; 94.10% used; 114348431 free inodes.

server4 `/data`: 89858990080 available bytes; 98.76% used; 225266582 free inodes.

server4 `/tmp`: 105650802688 available bytes; 94.10% used; 114348431 free inodes.

server4 `/var/tmp`: 105650802688 available bytes; 94.10% used; 114348431 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
