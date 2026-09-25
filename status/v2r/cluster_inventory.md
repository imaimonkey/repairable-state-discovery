# V2R cluster inventory

2026-09-25T03:19:03.078627+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318938882048 available bytes; 82.21% used; 112480359 free inodes.

server1 `/home`: 318938882048 available bytes; 82.21% used; 112480359 free inodes.

server1 `/tmp`: 318938882048 available bytes; 82.21% used; 112480359 free inodes.

server1 `/var/tmp`: 318938882048 available bytes; 82.21% used; 112480359 free inodes.

server1 `/mnt/raid5`: 416113774592 available bytes; 98.09% used; 337600221 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22989332480 available bytes; 98.72% used; 110410452 free inodes.

server2 `/home`: 22989332480 available bytes; 98.72% used; 110410452 free inodes.

server2 `/tmp`: 22989332480 available bytes; 98.72% used; 110410452 free inodes.

server2 `/var/tmp`: 22989332480 available bytes; 98.72% used; 110410452 free inodes.

server2 `/mnt/raid5`: 465239539712 available bytes; 96.79% used; 445112214 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84342624256 available bytes; 95.29% used; 114156075 free inodes.

server3 `/home`: 84342624256 available bytes; 95.29% used; 114156075 free inodes.

server3 `/data`: 144709611520 available bytes; 98.00% used; 225810125 free inodes.

server3 `/tmp`: 84342624256 available bytes; 95.29% used; 114156075 free inodes.

server3 `/var/tmp`: 84342624256 available bytes; 95.29% used; 114156075 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105692651520 available bytes; 94.10% used; 114350897 free inodes.

server4 `/home`: 105692651520 available bytes; 94.10% used; 114350897 free inodes.

server4 `/data`: 45425373184 available bytes; 99.37% used; 224966964 free inodes.

server4 `/tmp`: 105692651520 available bytes; 94.10% used; 114350897 free inodes.

server4 `/var/tmp`: 105692651520 available bytes; 94.10% used; 114350897 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
