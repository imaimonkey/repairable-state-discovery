# V2R cluster inventory

2026-09-27T02:17:16.606627+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315159760896 available bytes; 82.42% used; 112443335 free inodes.

server1 `/home`: 315159760896 available bytes; 82.42% used; 112443335 free inodes.

server1 `/tmp`: 315159760896 available bytes; 82.42% used; 112443335 free inodes.

server1 `/var/tmp`: 315159760896 available bytes; 82.42% used; 112443335 free inodes.

server1 `/mnt/raid5`: 637265289216 available bytes; 97.08% used; 337401675 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17628282880 available bytes; 99.02% used; 110365004 free inodes.

server2 `/home`: 17628282880 available bytes; 99.02% used; 110365004 free inodes.

server2 `/tmp`: 17628282880 available bytes; 99.02% used; 110365004 free inodes.

server2 `/var/tmp`: 17628282880 available bytes; 99.02% used; 110365004 free inodes.

server2 `/mnt/raid5`: 581340643328 available bytes; 95.98% used; 444885018 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78710284288 available bytes; 95.61% used; 114062953 free inodes.

server3 `/home`: 78710284288 available bytes; 95.61% used; 114062953 free inodes.

server3 `/data`: 1337721683968 available bytes; 81.51% used; 225762501 free inodes.

server3 `/tmp`: 78710284288 available bytes; 95.61% used; 114062953 free inodes.

server3 `/var/tmp`: 78710284288 available bytes; 95.61% used; 114062953 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105810264064 available bytes; 94.10% used; 114347750 free inodes.

server4 `/home`: 105810264064 available bytes; 94.10% used; 114347750 free inodes.

server4 `/data`: 400395476992 available bytes; 94.47% used; 224781819 free inodes.

server4 `/tmp`: 105810264064 available bytes; 94.10% used; 114347750 free inodes.

server4 `/var/tmp`: 105810264064 available bytes; 94.10% used; 114347750 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
