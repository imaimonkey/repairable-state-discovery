# V2R cluster inventory

2026-09-25T21:18:57.030382+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318703939584 available bytes; 82.22% used; 112476321 free inodes.

server1 `/home`: 318703939584 available bytes; 82.22% used; 112476321 free inodes.

server1 `/tmp`: 318703939584 available bytes; 82.22% used; 112476321 free inodes.

server1 `/var/tmp`: 318703939584 available bytes; 82.22% used; 112476321 free inodes.

server1 `/mnt/raid5`: 361445158912 available bytes; 98.34% used; 337539379 free inodes.
| server2 | True | ['6'] | [] | reference_compatible=False |

server2 `/`: 22896799744 available bytes; 98.72% used; 110405692 free inodes.

server2 `/home`: 22896799744 available bytes; 98.72% used; 110405692 free inodes.

server2 `/tmp`: 22896799744 available bytes; 98.72% used; 110405692 free inodes.

server2 `/var/tmp`: 22896799744 available bytes; 98.72% used; 110405692 free inodes.

server2 `/mnt/raid5`: 301345959936 available bytes; 97.92% used; 445055494 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84367208448 available bytes; 95.29% used; 114152628 free inodes.

server3 `/home`: 84367208448 available bytes; 95.29% used; 114152628 free inodes.

server3 `/data`: 125900107776 available bytes; 98.26% used; 225807181 free inodes.

server3 `/tmp`: 84367208448 available bytes; 95.29% used; 114152628 free inodes.

server3 `/var/tmp`: 84367208448 available bytes; 95.29% used; 114152628 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105389371392 available bytes; 94.12% used; 114347331 free inodes.

server4 `/home`: 105389371392 available bytes; 94.12% used; 114347331 free inodes.

server4 `/data`: 217848537088 available bytes; 96.99% used; 224920389 free inodes.

server4 `/tmp`: 105389371392 available bytes; 94.12% used; 114347331 free inodes.

server4 `/var/tmp`: 105389371392 available bytes; 94.12% used; 114347331 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
