# V2R cluster inventory

2026-09-25T04:37:39.462157+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318925729792 available bytes; 82.21% used; 112480362 free inodes.

server1 `/home`: 318925729792 available bytes; 82.21% used; 112480362 free inodes.

server1 `/tmp`: 318925729792 available bytes; 82.21% used; 112480362 free inodes.

server1 `/var/tmp`: 318925729792 available bytes; 82.21% used; 112480362 free inodes.

server1 `/mnt/raid5`: 408713850880 available bytes; 98.13% used; 337590790 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22946332672 available bytes; 98.72% used; 110410438 free inodes.

server2 `/home`: 22946332672 available bytes; 98.72% used; 110410438 free inodes.

server2 `/tmp`: 22946332672 available bytes; 98.72% used; 110410438 free inodes.

server2 `/var/tmp`: 22946332672 available bytes; 98.72% used; 110410438 free inodes.

server2 `/mnt/raid5`: 462813306880 available bytes; 96.80% used; 445109835 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84340224000 available bytes; 95.29% used; 114156076 free inodes.

server3 `/home`: 84340224000 available bytes; 95.29% used; 114156076 free inodes.

server3 `/data`: 143383584768 available bytes; 98.02% used; 225816007 free inodes.

server3 `/tmp`: 84340224000 available bytes; 95.29% used; 114156076 free inodes.

server3 `/var/tmp`: 84340224000 available bytes; 95.29% used; 114156076 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105664139264 available bytes; 94.10% used; 114350604 free inodes.

server4 `/home`: 105664139264 available bytes; 94.10% used; 114350604 free inodes.

server4 `/data`: 32784834560 available bytes; 99.55% used; 224962568 free inodes.

server4 `/tmp`: 105664139264 available bytes; 94.10% used; 114350604 free inodes.

server4 `/var/tmp`: 105664139264 available bytes; 94.10% used; 114350604 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
