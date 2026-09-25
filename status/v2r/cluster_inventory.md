# V2R cluster inventory

2026-09-25T04:59:13.244332+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318904426496 available bytes; 82.21% used; 112480365 free inodes.

server1 `/home`: 318904426496 available bytes; 82.21% used; 112480365 free inodes.

server1 `/tmp`: 318904426496 available bytes; 82.21% used; 112480365 free inodes.

server1 `/var/tmp`: 318904426496 available bytes; 82.21% used; 112480365 free inodes.

server1 `/mnt/raid5`: 409904865280 available bytes; 98.12% used; 337596264 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22939287552 available bytes; 98.72% used; 110410440 free inodes.

server2 `/home`: 22939287552 available bytes; 98.72% used; 110410440 free inodes.

server2 `/tmp`: 22939287552 available bytes; 98.72% used; 110410440 free inodes.

server2 `/var/tmp`: 22939287552 available bytes; 98.72% used; 110410440 free inodes.

server2 `/mnt/raid5`: 462127091712 available bytes; 96.81% used; 445108769 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84339757056 available bytes; 95.29% used; 114156076 free inodes.

server3 `/home`: 84339757056 available bytes; 95.29% used; 114156076 free inodes.

server3 `/data`: 142978355200 available bytes; 98.02% used; 225815585 free inodes.

server3 `/tmp`: 84339757056 available bytes; 95.29% used; 114156076 free inodes.

server3 `/var/tmp`: 84339757056 available bytes; 95.29% used; 114156076 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105659412480 available bytes; 94.10% used; 114350405 free inodes.

server4 `/home`: 105659412480 available bytes; 94.10% used; 114350405 free inodes.

server4 `/data`: 27943391232 available bytes; 99.61% used; 224961238 free inodes.

server4 `/tmp`: 105659412480 available bytes; 94.10% used; 114350405 free inodes.

server4 `/var/tmp`: 105659412480 available bytes; 94.10% used; 114350405 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
